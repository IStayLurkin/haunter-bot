import logging
import sys
import os
import re
from colorama import Fore, Style

# 🔒 Nuke all pre-existing handlers immediately
for h in logging.root.handlers[:]:
    logging.root.removeHandler(h)

# 🔇 Kill all handlers on discord-related loggers before they're initialized
for name in ["discord", "discord.client", "discord.gateway"]:
    logging.getLogger(name).handlers.clear()

# ✅ Set up logger before discord imports
from logger_setup import init_logger
init_logger()

# ✅ Now import discord
import discord

# Fix Windows path handling and add llama.cpp & gpt4all DLL directories
os.environ["LLAMACPP_MODEL_PATH"] = r"F:\\Projects\\haun\\models"
os.add_dll_directory(r"F:\\Projects\\haun\\llama.cpp\\build\\bin\\Release")
os.add_dll_directory(r"C:\\Users\\btayl\\gpt4all\\lib")
os.add_dll_directory(r"C:\\Python313\\Lib\\site-packages\\bin")
os.add_dll_directory(r"C:\\Python313\\Lib\\site-packages\\llama_cpp\\lib")

# Ensure local modules are importable
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Disable llama-related logs *before any other imports use them*
logging.getLogger("tools.llama_cpp").setLevel(logging.DEBUG)
logging.getLogger("tools.ollama_tool").setLevel(logging.DEBUG)
logging.getLogger("llama_cpp").setLevel(logging.DEBUG)
logging.getLogger("ollama_tool").setLevel(logging.DEBUG)

# Fully disable tool logs
logging.getLogger("tools.gpt4all").disabled = True
logging.getLogger("tools.llama_cpp").disabled = True
logging.getLogger("tools.ollama_tool").disabled = True

from config.constants import CONTEXT_LIMIT
import asyncio
import random
from collections import defaultdict
from typing import List
import shlex

from discord.ext import commands
from dotenv import load_dotenv

from llm_manager import get_llm
from memory import memory
from tool_registry import TOOLS
from utils.token_utils import truncate_to_token_limit
from llama_local import query_llama_local

# Force logging errors to stdout
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] %(levelname)-8s %(name)s: %(message)s')
handler.setFormatter(formatter)

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(handler)

# ---------------------------------------------------------------------------
# Environment & constants
# ---------------------------------------------------------------------------
load_dotenv()

MAX_HISTORY = int(os.getenv("OPENAI_MAX_HISTORY_MSGS", 100000))
MAX_DISCORD_CHARS = 1900

YOUR_USER_ID = 212698599631355904
HAUNTER_BOT_USER_ID = 1365583428610691082
KIB_BOT_ID = 1364340036492853248
YOUR_SHARED_CHANNEL_ID = 1364155387154272258

_raw_fc = os.getenv("KIBA_FREEFORM_CHANNELS", str(YOUR_SHARED_CHANNEL_ID))
FREEFORM_MATCH_ALL = _raw_fc.strip() == "*"
FREEFORM_CHANNELS = set() if FREEFORM_MATCH_ALL else {int(cid) for cid in _raw_fc.split(",") if cid}

# ---------------------------------------------------------------------------
# Runtime state
# ---------------------------------------------------------------------------
conversation_histories: defaultdict[int, List[str]] = defaultdict(list)
channel_topics: defaultdict[int, List[str]] = defaultdict(list)

persona_cache = {
    KIB_BOT_ID: (
        "You are Kib — a calm, encouraging assistant who explains things clearly "
        "and concisely. You avoid sarcasm or combative language and aim for a "
        "supportive, professional tone at all times. You love hacking and taking things to the next level always in pursuit of knowledge."
    ),
    HAUNTER_BOT_USER_ID: (
        "You are Haun — reserved and concise, but always polite and respectful. "
        "You never use snark; instead you deliver short, neutral answers that "
        "help the user without attitude. You love hacking and taking things to the next level always in pursuit of knowledge."
    ),
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def chunk(text: str) -> List[str]:
    text = text.strip()
    if not text:
        return ["[empty]"]
    return [text[i : i + MAX_DISCORD_CHARS] for i in range(0, len(text), MAX_DISCORD_CHARS)]

async def generate_response(bot_id: int, channel_id: int, user_message: str) -> str:
    persona = persona_cache.get(bot_id, "You are a helpful Discord bot.")
    recent_mem = memory.get_recent(1000)
    session = conversation_histories[channel_id][-10:]
    full_history = "\n".join(recent_mem + session)

    context_limit = CONTEXT_LIMIT
    usable_tokens = context_limit - 512  # reserve tokens for user + response

    trimmed_prompt = truncate_to_token_limit(
        f"{persona}\n\nConversation so far:\n{full_history}\n\nUser: {user_message}\nBot:", usable_tokens
    )

    llm = get_llm()
    reply = await asyncio.to_thread(llm.generate_text, trimmed_prompt, max_tokens=256)
    return reply

# ---------------------------------------------------------------------------
# Discord setup
# ---------------------------------------------------------------------------
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=None, intents=intents)
# ---------------------------------------------------------------------------
# Free-form tool executor
# ---------------------------------------------------------------------------
def _try_execute_tool(message_content: str) -> str | None:
    lowered = message_content.lower().strip()
    aliases = {
        "image": "stable_diffusion",
        "img": "stable_diffusion",
        "draw": "stable_diffusion",
        "sd": "stable_diffusion",
        "dalle": "openai_dall_e",
        "dall-e": "openai_dall_e",
    }
    for alias, tool_name in aliases.items():
        if lowered == alias or lowered.startswith(alias + " "):
            prompt = message_content[len(alias):].strip()
            out = TOOLS[tool_name](prompt)
            return f"[{tool_name}]\n{out}"
    for name in TOOLS:
        if lowered.startswith(name.lower()):
            arg = message_content[len(name):].strip()
            out = TOOLS[name](arg)
            return f"[{name}]\n{out}"
    return None

# ---------------------------------------------------------------------------
# Events
# ---------------------------------------------------------------------------

@bot.event
async def on_message(message: discord.Message):
    log = logging.getLogger("discord.client")
    log.debug(f"[MESSAGE RECEIVED] {message.author.name}: {message.content}")

    try:
        if message.author.id == bot.user.id:
            return

        content = message.content.strip()
        channel_id = message.channel.id
        bot_name_lower = bot.user.name.lower()
        mentioned = bot_name_lower in content.lower()
        freeform_allowed = FREEFORM_MATCH_ALL or (channel_id in FREEFORM_CHANNELS)

        log.debug(f"[INPUT] {message.author.name}: {content}")
        memory.add(f"{message.author.name}: {content}")

        log.debug("→ Entering: LLaMA freeform block")
        if freeform_allowed or mentioned:
            log.debug("[EVENT] Freeform allowed or bot mentioned.")
            from llama_local import query_llama_local

            async with message.channel.typing():
                response = await query_llama_local(content)

                if callable(getattr(response, "__await__", None)):
                    log.warning("⚠️ Response is coroutine — awaiting it")
                    response = await response

                if not isinstance(response, str):
                    log.error(f"[TYPE ERROR] Non-string response: {type(response)} — {repr(response)}")
                    response = "[LLaMA Error]"

                await message.channel.send(response[:2000])
            return

    except Exception as e:
        log.error("💥 Unhandled exception in on_message:", exc_info=True)
        try:
            await message.channel.send("⚠️ Internal error — check logs.")
        except:
            pass
    log.debug("→ Entering: Google image search block")
    # Free-form Google Images search
    if freeform_allowed:
        m = re.search(
            r'\\b(?:google|search for|find|look up)\\b.*\\b(?:pic|picture|image)s?\\b of (.+)',
            content, flags=re.IGNORECASE
        )
        if m:
            q = m.group(1).strip()
            async with message.channel.typing():
                res = TOOLS["google_images_search"](q).strip()
                if res.startswith(("http://", "https://")):
                    await message.channel.send(res)
                else:
                    for c in chunk(f"```{res}```"):
                        await message.channel.send(c)
            return
    log.debug("→ Entering: SD image generation block")
    # Free-form image generation
    if freeform_allowed:
        m2 = re.search(
            r'\\b(?:draw|show me|generate|gen|create)\\b.*\\b(?:pic|picture|image)s?\\b(?: of)? (.+)',
            content, flags=re.IGNORECASE
        )
        if m2:
            q = m2.group(1).strip()
            async with message.channel.typing():
                img = TOOLS["stable_diffusion"](q).strip()
                if img.startswith(("http://", "https://")):
                    await message.channel.send(img)
                else:
                    for c in chunk(f"```{img}```"):
                        await message.channel.send(c)
            return
    log.debug("→ Entering: Freeform generic tool block")
    # Free-form generic tool execution
    if freeform_allowed:
        tool_out = _try_execute_tool(content)
        if tool_out:
            async with message.channel.typing():
                for part in chunk(tool_out):
                    await message.channel.send(part)
            return
    log.debug("→ Entering: !tool command block")
    # Explicit !tool commands
    if content.startswith("!tool "):
        _, tool_name, *argp = content.split(" ", 2)
        arg = argp[0] if argp else ""
        async with message.channel.typing():
            if tool_name in TOOLS:
                out = TOOLS[tool_name](arg).strip()
                lines = out.splitlines()
                if all(line.startswith(("http://", "https://")) for line in lines):
                    embeds = [discord.Embed().set_image(url=url) for url in lines]
                    await message.channel.send(embeds=embeds[:10])
                else:
                    for c in chunk(f"```{out}```"):
                        await message.channel.send(c)
            else:
                await message.channel.send(f"Tool `{tool_name}` not found.")
        return
    log.debug("→ Entering: Chat/mention generate_response block")
    # Chat / mention handling
    if mentioned or freeform_allowed:
        conversation_histories[channel_id].append(f"{message.author.name}: {content}")
        conversation_histories[channel_id] = conversation_histories[channel_id][-MAX_HISTORY:]
        memory.add(f"{message.author.name}: {content}")

        async with message.channel.typing():
            reply = await generate_response(bot.user.id, channel_id, content)
            if mentioned:
                reply = f"Yes, this is {bot.user.name}. " + reply
            for part in chunk(reply):
                await message.channel.send(part)

        conversation_histories[channel_id].append(f"Bot: {reply}")
        conversation_histories[channel_id] = conversation_histories[channel_id][-MAX_HISTORY:]
        memory.add(f"Bot: {reply}")

@bot.command(name="recall")
async def recall_memory(ctx):
    entries = memory.get_recent(20)
    if not entries:
        await ctx.send("Memory is empty.")
        return

    reply = "\n".join(entries)
    for part in chunk(reply):
        await ctx.send(f"```{part}```")

# ---------------------------------------------------------------------------
@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error):
    if isinstance(error, discord.app_commands.CommandNotFound):
        return
    log.error(error)

# ---------------------------------------------------------------------------
if __name__ == "__main__":
    token = os.getenv("DISCORD_TOKEN_HAUNTER")
    if not token:
        raise RuntimeError("DISCORD_TOKEN_HAUNTER not set in environment or .env")
    bot.run(token)
