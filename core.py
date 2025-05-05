# core.py
# Console-based interface for your LLM-powered bot with tool integration

import os
import sys
from dotenv import load_dotenv
from llm_manager import get_llm
from memory import memory
from tool_registry import TOOLS, list_tools

# Load .env variables if present
global_env = os.getcwd()
load_dotenv(dotenv_path=os.path.join(global_env, '.env'))


def run_tool_cli(tool_name: str, arg: str):
    """Run a single tool invocation and exit."""
    if tool_name in TOOLS:
        result = TOOLS[tool_name](arg)
        print(result)
    else:
        print(f"Tool '{tool_name}' not found. Available: {list_tools()}")
    sys.exit(0)


def interactive_loop():
    llm = get_llm()
    print("Available tools:", list_tools())
    while True:
        try:
            inp = input("You> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break

        if not inp:
            continue

        if inp.startswith("!tool "):
            parts = inp.split(maxsplit=2)
            if len(parts) < 3:
                print("Usage: !tool <name> <arg>")
            else:
                _, tool_name, arg = parts
                if tool_name in TOOLS:
                    print(TOOLS[tool_name](arg))
                else:
                    print(f"Tool '{tool_name}' not found.")
        else:
            # LLM chat with memory
            memory.add(f"You: {inp}")
            history = "\n".join(memory.recall()) + "\nBot:"
            resp = llm.generate(history)
            print("Bot>", resp)
            memory.add(f"Bot: {resp}")


if __name__ == "__main__":
    # CLI mode: python core.py <tool_name> <arg>
    if len(sys.argv) > 1:
        tool_name = sys.argv[1]
        arg = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""
        run_tool_cli(tool_name, arg)
    else:
        interactive_loop()
