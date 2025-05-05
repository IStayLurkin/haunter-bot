import os
import importlib.util

def generate_command_code(tool_name):
    command = tool_name.lower()
    code = f"""
    elif content.startswith("!{command}"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "{tool_name}" in TOOLS:
                result = TOOLS["{tool_name}"](arg)
                for part in chunk(f'```{{result}}```'):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `{tool_name}` not found.")
        return
"""
    return code

def main():
    current_dir = os.getcwd()
    print(f"Current working directory: {current_dir}")
    tools_dir_kib = r"F:\Projects\haun\tools"
    tools_dir_haun = r"F:\Projects\haun\tools"
    generated_code_kiba = []
    generated_code_haunter = []

    if not os.path.isdir(tools_dir_kib):
        print(f"Error: Tools directory not found for Kiba at {tools_dir_kib}")
        return

    if not os.path.isdir(tools_dir_haun):
        print(f"Error: Tools directory not found for Haunter at {tools_dir_haun}")
        return

    for filename in os.listdir(tools_dir_kib):
        if filename.endswith(".py") and filename != "__init__.py":
            tool_name_without_ext = filename[:-3]
            command_code = generate_command_code(tool_name_without_ext)
            generated_code_kiba.append(command_code)

    for filename in os.listdir(tools_dir_haun):
        if filename.endswith(".py") and filename != "__init__.py":
            tool_name_without_ext = filename[:-3]
            command_code = generate_command_code(tool_name_without_ext)
            generated_code_haunter.append(command_code)

    print("\n--- Code snippets to add to Kiba Bot's on_message function: ---\n")
    for code in generated_code_kiba:
        print(code)

    print("\n--- Code snippets to add to Haunter Bot's on_message function: ---\n")
    for code in generated_code_haunter:
        print(code)

if __name__ == "__main__":
    main()