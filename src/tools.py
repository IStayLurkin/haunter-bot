import logging
import json
import datetime
import subprocess # For execute_shell example
import os # For execute_shell example

# --- Tool Implementation Examples ---
# Add your custom tool functions here.
# They should accept arguments as defined in TOOL_DESCRIPTIONS
# and return a string result.

def get_current_datetime(**kwargs) -> str:
    """
    Returns the current date and time.
    Ignores any arguments passed via kwargs.
    """
    now = datetime.datetime.now()
    return f"The current date and time is: {now.strftime('%Y-%m-%d %H:%M:%S')}"

def get_current_location(**kwargs) -> str:
    """
    Returns the known current location.
    In this simple example, it's hardcoded based on context.
    A real implementation might use IP geolocation, GPS, or user settings.
    Ignores any arguments passed via kwargs.
    """
    # NOTE: Hardcoded based on the initial prompt context provided.
    # Replace with dynamic logic if needed.
    return "Happy Valley, Oregon, United States"

def simple_osint_search(query: str, **kwargs) -> str:
    """
    Placeholder for a basic OSINT tool. Simulates searching for information.
    A real tool would use web scraping (requests, beautifulsoup4), APIs, etc.
    Args:
        query (str): The search term or question.
    Returns:
        str: A simulated search result or a 'not found' message.
    """
    logging.info(f"Executing OSINT search for query: '{query}'")
    query_lower = query.lower()
    location = get_current_location() # Can call other tools internally if needed

    # ** Replace this with actual OSINT logic **
    if "weather" in query_lower:
        # Simulate weather based on location
        if "happy valley" in location.lower():
             return f"Simulated weather for {location}: Partly cloudy, 15°C."
        else:
             return f"Simulated weather for {location}: Sunny, 20°C."
    elif "news" in query_lower and "happy valley" in query_lower:
        return f"Simulated news for {location}: Local council discusses new park proposal. Upcoming farmers market this weekend."
    elif "events" in query_lower and "happy valley" in query_lower:
        return f"Simulated events in {location}: Farmers Market (Sat), Community Garage Sale (Sun)."
    else:
        # Generic placeholder response
        return f"OSINT Tool Simulation: No specific information found for '{query}'. Try queries like 'weather in Happy Valley' or 'news Happy Valley'."

def execute_shell_command(command: str, **kwargs) -> str:
    """
    Executes a shell command provided as a string.
    !!! EXTREME CAUTION !!! Running arbitrary commands is a major security risk.
    This should ONLY be enabled in highly controlled environments and ideally
    with strict input validation or whitelisting of allowed commands.
    Args:
        command (str): The shell command to execute.
    Returns:
        str: The standard output and standard error of the command, or an error message.
    """
    logging.warning(f"Attempting to execute shell command: '{command}'")

    # --- !!! SECURITY WARNING !!! ---
    # Add rigorous checks here before enabling this tool in any production
    # or shared environment. Whitelisting safe commands is much safer
    # than trying to blacklist unsafe ones.
    # Example (very basic - needs improvement):
    # allowed_commands = ['ls', 'pwd', 'echo']
    # if not any(command.strip().startswith(ac) for ac in allowed_commands):
    #     logging.error(f"Shell command blocked for security reasons: {command}")
    #     return "Error: Command not allowed for security reasons."
    # --- !!! END SECURITY WARNING !!! ---

    if not command:
        return "Error: No command provided to execute_shell_command."

    try:
        # Setting shell=True is risky. Avoid if possible. If needed, sanitize 'command' carefully.
        # Consider using list format: subprocess.run(['ls', '-l'], ...) which is safer.
        result = subprocess.run(
            command,
            shell=True, # Be very careful with shell=True
            capture_output=True,
            text=True,
            timeout=15, # Set a timeout
            check=False, # Don't raise exception on non-zero exit code, report it instead
            cwd=os.path.expanduser("~") # Run in user's home directory for safety? Or project root?
        )

        output = f"Exit Code: {result.returncode}\n"
        if result.stdout:
            output += f"STDOUT:\n{result.stdout.strip()}\n"
        if result.stderr:
            output += f"STDERR:\n{result.stderr.strip()}"

        # Limit output length to avoid overwhelming the LLM context
        max_len = 1500
        if len(output) > max_len:
            output = output[:max_len] + "\n... (output truncated)"
        return output.strip()

    except subprocess.TimeoutExpired:
        logging.error(f"Shell command timed out: {command}")
        return "Error: Command execution timed out."
    except Exception as e:
        logging.error(f"Error executing shell command '{command}': {e}", exc_info=True)
        return f"Error: Failed to execute command. Reason: {e}"


# --- Tool Registry and Descriptions ---

# 1. Register your functions here: Map a tool name (used by LLM) to the function object.
TOOL_REGISTRY = {
    "get_current_datetime": get_current_datetime,
    "get_current_location": get_current_location,
    "simple_osint_search": simple_osint_search,
    # "execute_shell_command": execute_shell_command, # <-- Add with extreme caution!
}

# 2. Describe your tools clearly for the LLM.
#    - Use the exact tool names from TOOL_REGISTRY.
#    - Specify arguments (name and type) accurately.
#    - Explain what the tool does and when to use it.
#    - Keep descriptions concise but informative.
TOOL_DESCRIPTIONS = """
You have access to the following tools to gather information or perform actions:

- get_current_datetime():
    Description: Returns the current date and time.
    Arguments: None.
    Use when: The user asks for the current date, time, or day.

- get_current_location():
    Description: Returns the user's current known location (city, state, country).
    Arguments: None.
    Use when: The user asks about their location, or needs location-specific info (like weather) and hasn't specified a location.

- simple_osint_search(query: str):
    Description: Performs a basic simulated search for information based on the provided query string. Good for finding current information like weather, local news, or events in the current location if not specified in the query.
    Arguments:
      - query (str): The search term or question (e.g., "weather", "local news", "events this weekend").
    Use when: The user asks for information that requires up-to-date knowledge, like weather forecasts, recent news headlines, or local event schedules. Be specific in the query.

**How to Use Tools:**
When you decide to use a tool, respond *only* with a single JSON object in the following format. Do not include any other text before or after the JSON object.
```json
{
  "tool_name": "<name_of_the_tool_to_use>",
  "arguments": {
    "<argument_name_1>": "<value1>",
    "<argument_name_2>": "<value2>"
  }
}
```
If a tool takes no arguments, provide an empty "arguments" object: `"arguments": {}`.
If you can answer the user's query without using a tool, respond directly in plain text.
"""
# - execute_shell_command(command: str): # <-- Add description with caution if enabling
#     Description: Executes a given shell command string on the host system. DANGEROUS - USE WITH EXTREME CAUTION. Only use for simple, safe, read-only commands if absolutely necessary (e.g., 'ls', 'pwd'). Do not use for commands that modify files or system settings.
#     Arguments:
#       - command (str): The shell command to execute (e.g., "ls -l /tmp").
#     Use when: Specifically asked to perform a simple, safe command-line operation by the user, and only if deemed safe. Prefer other tools if possible.


def get_tool_descriptions() -> str:
    """Returns the formatted descriptions of available tools."""
    # In a more advanced system, this could be generated dynamically from docstrings
    # or a more structured tool definition format.
    return TOOL_DESCRIPTIONS

def format_tool_prompt(system_message: str) -> str:
    """Adds tool usage instructions and descriptions to the system prompt."""
    # Only add tool info if tools are enabled in the registry
    if not TOOL_REGISTRY:
        return system_message
    return f"{system_message}\n\n{TOOL_DESCRIPTIONS}"


def execute_tool(tool_call_json: str, config: dict) -> tuple[str | None, str | None]:
    """
    Parses a JSON string presumed to be a tool call from the LLM,
    executes the corresponding tool function, and returns the result.

    Args:
        tool_call_json (str): The JSON string received from the LLM.
        config (dict): The application configuration (might be needed by tools).

    Returns:
        tuple[str | None, str | None]: A tuple containing:
            - tool_name (str): The name of the tool that was called, or None if parsing failed or it wasn't a tool call.
            - result (str): The string output from the tool, or an error message if execution failed. None if not a tool call.
    """
    if not config.get('tools', {}).get('enabled', False):
        logging.warning("Tool execution attempted but tools are disabled in config.")
        # Return None, None because it wasn't a *valid* tool call attempt in this state
        return None, None

    try:
        # Attempt to parse the LLM response as JSON
        tool_call = json.loads(tool_call_json)

        # Validate the basic structure
        tool_name = tool_call.get('tool_name')
        arguments = tool_call.get('arguments', {}) # Default to empty dict if missing

        if not isinstance(tool_name, str) or not isinstance(arguments, dict):
            logging.warning(f"LLM response parsed as JSON but lacks 'tool_name' (string) or 'arguments' (dict): {tool_call_json[:200]}")
            return None, None # Not a valid tool call format

        # Check if the requested tool exists in our registry
        if tool_name in TOOL_REGISTRY:
            tool_function = TOOL_REGISTRY[tool_name]
            logging.info(f"Executing tool '{tool_name}' with arguments: {arguments}")

            try:
                # Execute the tool function with the provided arguments
                # Pass config in case the tool needs it (though explicit args are better)
                result = tool_function(**arguments, config=config) # Pass config as a potential kwarg
                result_str = str(result) # Ensure the result is a string

                # Basic check for excessively long results
                max_result_len = 4000 # Limit tool output length
                if len(result_str) > max_result_len:
                     logging.warning(f"Tool '{tool_name}' output truncated from {len(result_str)} to {max_result_len} chars.")
                     result_str = result_str[:max_result_len] + "... (truncated)"

                logging.info(f"Tool '{tool_name}' executed successfully.")
                return tool_name, result_str # Return tool name and its string result

            except TypeError as e:
                 # Handles cases where arguments don't match the function signature
                 logging.error(f"TypeError executing tool '{tool_name}' with args {arguments}. Check arguments/function definition. Error: {e}", exc_info=True)
                 return tool_name, f"Error: Invalid arguments provided for tool '{tool_name}'. Required arguments might be missing or incorrect. Details: {e}"
            except Exception as e:
                 # Catch other exceptions during tool execution
                 logging.error(f"Exception executing tool '{tool_name}': {e}", exc_info=True)
                 return tool_name, f"Error: Failed to execute tool '{tool_name}'. Reason: {e}"
        else:
            # LLM hallucinated a tool name or requested one not registered
            logging.warning(f"LLM requested unknown tool: '{tool_name}'")
            return tool_name, f"Error: The tool '{tool_name}' is not available."

    except json.JSONDecodeError:
        # The LLM response was not valid JSON, so it's likely a normal text response
        logging.debug("LLM response is not a JSON tool call.")
        return None, None # Indicate it wasn't a tool call
    except Exception as e:
        # Catch unexpected errors during the parsing/checking phase
        logging.error(f"Unexpected error processing potential tool call: {e}", exc_info=True)
        return None, "Error: Could not process the potential tool request due to an unexpected error."

