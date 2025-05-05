import logging
from .llm_interface import LLMInterface
from .memory import ChatMemory
from .tools import execute_tool, format_tool_prompt # Import tool functions

def run_cli_loop(config: dict, llm: LLMInterface, memory: ChatMemory):
    """
    Runs the main command-line interaction loop for the bot.

    Args:
        config (dict): The application configuration.
        llm (LLMInterface): The initialized LLM interface.
        memory (ChatMemory): The initialized chat memory handler.
    """
    print("\n--- Offline Bot CLI ---")
    print(f"Model: {llm.get_model_name()}")
    print("Type 'quit' to exit, 'clear' to reset memory.")
    print("-" * 25)

    tools_enabled = config.get('tools', {}).get('enabled', False)
    max_tool_iterations = 3 # Prevent infinite tool loops

    while True:
        try:
            user_input = input("User: ")
        except EOFError: # Handle Ctrl+D
            print("\nExiting...")
            break

        if not user_input:
            continue

        if user_input.lower() == 'quit':
            print("Exiting CLI.")
            break
        if user_input.lower() == 'clear':
            memory.clear_history()
            print("Memory cleared.")
            continue

        # Add user message to memory
        memory.add_message("user", user_input)

        current_tool_iterations = 0
        while current_tool_iterations < max_tool_iterations:
            # Prepare message history for the LLM
            history = memory.get_history()
            messages_for_llm = []

            # Construct system prompt (only once or based on model needs)
            system_message = "You are a helpful offline assistant."
            if tools_enabled:
                system_message = format_tool_prompt(system_message) # Add tool instructions

            # Check if history is empty or only contains the system prompt idea
            # A simple approach: always prepend the system message if tools are enabled,
            # or if the history doesn't seem to have one. LLM should handle it.
            # More sophisticated logic might be needed depending on the model.
            if not any(m['role'] == 'system' for m in history):
                 messages_for_llm.append({"role": "system", "content": system_message})

            messages_for_llm.extend(history) # Add the actual conversation history

            # --- Get response from LLM ---
            print("Bot: Thinking...")
            try:
                llm_response_text = llm.generate_response_with_history(messages_for_llm)
            except Exception as e:
                 logging.error(f"LLM generation failed: {e}", exc_info=True)
                 print("Bot: Sorry, I encountered an error generating a response.")
                 # Break out of the tool loop on LLM error
                 break # Go to next user input

            # --- Tool Execution Check ---
            tool_name, tool_result = None, None
            if tools_enabled:
                tool_name, tool_result = execute_tool(llm_response_text, config)

            if tool_name and tool_result:
                # A tool was called (successfully or with an error message)
                print(f"Bot: (Attempting to use tool '{tool_name}'...)")
                logging.info(f"Tool '{tool_name}' called. Result: {tool_result[:100]}...")

                # Add the LLM's request and the tool's result to memory
                memory.add_message("assistant", llm_response_text) # Save the raw tool call JSON
                memory.add_message("tool", tool_result) # Save the tool's output/error

                current_tool_iterations += 1
                if current_tool_iterations >= max_tool_iterations:
                     print("Bot: Reached maximum tool iterations. Providing final response.")
                     # Let the loop break and generate a final response based on the last tool result
                     break
                # Continue the inner loop to let the LLM process the tool result
                continue
            else:
                # No valid tool call detected, or tools disabled. This is the final response.
                print(f"Bot: {llm_response_text}")
                memory.add_message("assistant", llm_response_text)
                # Break the inner tool loop as we have the final response
                break
        else:
             # This else block executes if the while loop completes without break (i.e., max iterations reached)
             # Need to generate a final response based on the last tool result stored in memory
             history = memory.get_history()
             messages_for_llm = []
             system_message = "You are a helpful offline assistant."
             if tools_enabled: system_message = format_tool_prompt(system_message)
             if not any(m['role'] == 'system' for m in history): messages_for_llm.append({"role": "system", "content": system_message})
             messages_for_llm.extend(history)

             print("Bot: Thinking (final response after max tools)...")
             try:
                 final_response = llm.generate_response_with_history(messages_for_llm)
                 print(f"Bot: {final_response}")
                 memory.add_message("assistant", final_response)
             except Exception as e:
                 logging.error(f"LLM generation failed on final response: {e}", exc_info=True)
                 print("Bot: Sorry, I encountered an error generating the final response.")


    print("\n--- CLI Session Ended ---")

