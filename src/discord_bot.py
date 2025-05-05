import discord
import logging
import asyncio
import threading
from .llm_interface import LLMInterface
from .memory import ChatMemory
from .tools import execute_tool, format_tool_prompt

# --- Per-Channel Memory Management ---
# Use a dictionary to store separate ChatMemory instances for each channel.
# Key: channel_id (int), Value: ChatMemory instance
channel_memory_instances = {}
memory_lock = threading.Lock() # Lock for accessing the channel_memory_instances dict

def get_or_create_channel_memory(channel_id: int, config: dict) -> ChatMemory:
    """
    Retrieves or creates a ChatMemory instance specific to a channel ID.
    Ensures thread safety when accessing the shared dictionary.

    Args:
        channel_id (int): The Discord channel ID.
        config (dict): The base application configuration.

    Returns:
        ChatMemory: The ChatMemory instance for the given channel.
    """
    with memory_lock:
        if channel_id not in channel_memory_instances:
            logging.info(f"Creating new memory instance for channel ID: {channel_id}")
            # Create a slightly modified config for this channel's memory path if desired
            channel_config = config.copy()
            base_mem_path = config['memory']['path']
            # Ensure path is absolute before modifying
            if not os.path.isabs(base_mem_path):
                 project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                 base_mem_path = os.path.join(project_root, base_mem_path)

            path_parts = os.path.splitext(base_mem_path)
            channel_mem_path = f"{path_parts[0]}_channel_{channel_id}{path_parts[1]}"

            # Make a deep copy of the memory config part if necessary
            channel_config['memory'] = config['memory'].copy()
            channel_config['memory']['path'] = channel_mem_path

            try:
                channel_memory_instances[channel_id] = ChatMemory(channel_config)
            except Exception as e:
                 logging.error(f"Failed to create memory for channel {channel_id} at {channel_mem_path}: {e}", exc_info=True)
                 # Fallback to a default shared memory? Or raise error? Raising for now.
                 raise RuntimeError(f"Could not initialize memory for channel {channel_id}") from e
        else:
             logging.debug(f"Reusing existing memory instance for channel ID: {channel_id}")

        return channel_memory_instances[channel_id]

# --- Discord Client Setup ---

class OfflineBotClient(discord.Client):
    def __init__(self, *, intents: discord.Intents, config: dict, llm: LLMInterface):
        super().__init__(intents=intents)
        self.config = config
        self.llm = llm
        self.tools_enabled = config.get('tools', {}).get('enabled', False)
        self.allowed_channel_ids = {int(cid) for cid in config.get('discord', {}).get('allowed_channel_ids', []) if cid}
        self.max_tool_iterations = 3 # Prevent infinite loops
        logging.info("Discord Client initialized.")
        if self.allowed_channel_ids:
            logging.info(f"Restricting activity to channels: {self.allowed_channel_ids}")
        else:
            logging.info("Bot will respond in any channel when mentioned (or in DMs).")

    async def on_ready(self):
        logging.info(f'Discord bot logged in as {self.user} (ID: {self.user.id})')
        print(f'Discord bot {self.user} is ready.')
        await self.change_presence(activity=discord.Game(name="with local LLMs"))

    async def on_message(self, message: discord.Message):
        # 1. Ignore messages from the bot itself
        if message.author == self.user:
            return

        # 2. Check if the bot should process this message
        is_dm = isinstance(message.channel, discord.DMChannel)
        is_mentioned = self.user.mentioned_in(message)
        is_allowed_channel = not self.allowed_channel_ids or message.channel.id in self.allowed_channel_ids

        # Determine if we should respond:
        # - Respond in DMs.
        # - Respond if mentioned in an allowed channel (if channels are specified).
        # - Respond if mentioned in *any* channel (if no channels are specified).
        should_respond = is_dm or (is_mentioned and is_allowed_channel)

        if not should_respond:
            # Log ignored messages only at debug level if needed
            # logging.debug(f"Ignoring message from {message.author} in channel {message.channel.id} (not mentioned or not allowed channel).")
            return

        # 3. Get message content, removing the mention
        content = message.content
        if is_mentioned:
             # Remove all forms of mention (@BotName, @!BotName)
             content = content.replace(f'<@{self.user.id}>', '').replace(f'<@!{self.user.id}>', '').strip()

        # Ignore empty messages after removing mention
        if not content:
            logging.debug(f"Ignoring empty message from {message.author} after mention removal.")
            return

        logging.info(f"Processing message from {message.author} in {'DM' if is_dm else 'Channel '+str(message.channel.id)}: '{content[:50]}...'")

        # 4. Get channel-specific memory
        # Use author ID for DMs to give users separate memory
        memory_key = message.author.id if is_dm else message.channel.id
        try:
            memory = get_or_create_channel_memory(memory_key, self.config)
        except RuntimeError:
            await message.reply("Sorry, I couldn't access the memory for this conversation.")
            return

        # 5. Handle special commands
        if content.lower() == 'clear memory':
            memory.clear_history()
            await message.reply("Conversation history for this chat has been cleared.")
            logging.info(f"Memory cleared for {'DM '+str(message.author.id) if is_dm else 'Channel '+str(message.channel.id)}")
            return

        # 6. Add user message to memory
        memory.add_message("user", content)

        # 7. Process with LLM and potential tools (using an inner loop)
        async with message.channel.typing(): # Show "Bot is typing..."
            current_tool_iterations = 0
            while current_tool_iterations < self.max_tool_iterations:
                # Prepare history for LLM
                history = memory.get_history()
                messages_for_llm = []
                system_message = "You are a helpful Discord bot assistant."
                if self.tools_enabled: system_message = format_tool_prompt(system_message)
                if not any(m['role'] == 'system' for m in history): messages_for_llm.append({"role": "system", "content": system_message})
                messages_for_llm.extend(history)

                # --- Call LLM (Run synchronously for simplicity, use executor for production) ---
                try:
                    # In a production bot, run blocking IO/CPU tasks in an executor:
                    # loop = asyncio.get_running_loop()
                    # llm_response_text = await loop.run_in_executor(
                    #     None, # Default executor
                    #     self.llm.generate_response_with_history,
                    #     messages_for_llm
                    # )
                    llm_response_text = self.llm.generate_response_with_history(messages_for_llm) # Sync call

                except Exception as e:
                    logging.error(f"LLM generation failed for channel {memory_key}: {e}", exc_info=True)
                    await message.reply("Sorry, I encountered an error while thinking.")
                    return # Stop processing this message

                # --- Tool Check (Run synchronously for simplicity) ---
                tool_name, tool_result = None, None
                if self.tools_enabled:
                    # loop = asyncio.get_running_loop()
                    # tool_name, tool_result = await loop.run_in_executor(
                    #      None, execute_tool, llm_response_text, self.config
                    # )
                    tool_name, tool_result = execute_tool(llm_response_text, self.config) # Sync call

                if tool_name and tool_result:
                    logging.info(f"Discord Bot: Tool '{tool_name}' called for channel {memory_key}. Result: {tool_result[:100]}...")
                    # Add tool request and result to memory
                    memory.add_message("assistant", llm_response_text) # Tool call JSON
                    memory.add_message("tool", tool_result) # Tool output/error

                    current_tool_iterations += 1
                    if current_tool_iterations >= self.max_tool_iterations:
                         logging.warning(f"Reached max tool iterations ({self.max_tool_iterations}) for channel {memory_key}.")
                         # Loop will break, then generate final response below
                         break
                    # Continue loop to let LLM process tool result
                    continue
                else:
                    # No tool called or tools disabled - this is the final response
                    memory.add_message("assistant", llm_response_text)
                    await self.send_reply(message, llm_response_text)
                    return # Finished processing this message

            # --- Handle Max Tool Iterations Reached ---
            if current_tool_iterations >= self.max_tool_iterations:
                 # Generate a final response based on the last tool result in memory
                 history = memory.get_history()
                 messages_for_llm = []
                 system_message = "You are a helpful Discord bot assistant."
                 if self.tools_enabled: system_message = format_tool_prompt(system_message)
                 if not any(m['role'] == 'system' for m in history): messages_for_llm.append({"role": "system", "content": system_message})
                 messages_for_llm.extend(history)

                 logging.info(f"Generating final response after max tool iterations for channel {memory_key}.")
                 try:
                     # loop = asyncio.get_running_loop()
                     # final_response = await loop.run_in_executor(None, self.llm.generate_response_with_history, messages_for_llm)
                     final_response = self.llm.generate_response_with_history(messages_for_llm) # Sync call
                     memory.add_message("assistant", final_response)
                     await self.send_reply(message, final_response)
                 except Exception as e:
                     logging.error(f"LLM generation failed on final response for channel {memory_key}: {e}", exc_info=True)
                     await message.reply("Sorry, I reached the tool limit and couldn't generate a final response.")


    async def send_reply(self, message: discord.Message, text: str):
        """Sends a reply, handling Discord's message length limits."""
        max_len = 2000 # Discord message limit
        if not text:
             text = "(Empty response from LLM)"

        if len(text) <= max_len:
            await message.reply(text, mention_author=False)
        else:
            logging.info(f"Response exceeds {max_len} chars, splitting into multiple messages.")
            parts = []
            current_part = ""
            # Split carefully, preferring newline boundaries
            for line in text.splitlines(keepends=True):
                 if len(current_part) + len(line) > max_len:
                      if current_part: parts.append(current_part)
                      # If a single line is too long, split it mid-line
                      if len(line) > max_len:
                           for i in range(0, len(line), max_len):
                                parts.append(line[i:i+max_len])
                           current_part = "" # Reset after splitting long line
                      else:
                           current_part = line
                 else:
                      current_part += line
            if current_part: parts.append(current_part) # Add the last part

            first = True
            for part in parts:
                 if first:
                      await message.reply(part, mention_author=False)
                      first = False
                 else:
                      # Send subsequent parts as regular messages in the channel
                      await message.channel.send(part)
                 await asyncio.sleep(0.5) # Small delay between parts


def run_discord_bot(config: dict, llm: LLMInterface):
    """Sets up and runs the Discord bot."""
    discord_config = config.get('discord', {})
    if not discord_config.get('enabled', False):
        logging.info("Discord bot is disabled in the configuration.")
        return

    token = discord_config.get('token')
    if not token or token == "YOUR_DISCORD_BOT_TOKEN":
        logging.error("Discord token is missing or invalid in config/environment variables. Cannot start Discord bot.")
        print("ERROR: Discord token missing. Set DISCORD_BOT_TOKEN environment variable or update config.yaml.")
        return

    # Define necessary intents
    intents = discord.Intents.default()
    intents.message_content = True # Required to read message content
    intents.messages = True        # Required for on_message
    intents.guilds = True          # Required for channel info

    client = OfflineBotClient(intents=intents, config=config, llm=llm)

    try:
        logging.info("Starting Discord bot...")
        client.run(token)
    except discord.LoginFailure:
        logging.error("Discord login failed: Invalid token.")
        print("ERROR: Discord login failed. Please check your bot token.")
    except discord.PrivilegedIntentsRequired:
         logging.error("Discord Privileged Intents (Message Content) are not enabled for the bot in the Discord Developer Portal.")
         print("ERROR: Message Content Intent not enabled. Go to your bot's settings in the Discord Developer Portal and enable it.")
    except Exception as e:
        logging.error(f"An unexpected error occurred while running the Discord bot: {e}", exc_info=True)
        print(f"ERROR: An unexpected error occurred: {e}")

# --- Helper for path resolution (needed by get_or_create_channel_memory) ---
import os
