import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

"""
 tool_integrator.py
 ------------------
 Renders Jinja2 templates over existing stub files in ./tools/.
 Supported strategies:
   • "specific" → render a hand‑written template file.
   • "rest"     → render templates/_generic_rest.py.j2 with cfg dict.
   • "cli"      → render templates/_generic_cli.py.j2  with cfg dict.

 Add or edit entries in TEMPLATE_MAP to light up more tools.
 Run:  python tool_integrator.py
"""

BASE_DIR       = Path(__file__).parent
TEMPLATES_DIR  = BASE_DIR / "templates"
TOOLS_DIR      = BASE_DIR / "tools"

env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), trim_blocks=True, lstrip_blocks=True)

# ---------------------------------------------------------------------------
# Template mapping
# ---------------------------------------------------------------------------
TEMPLATE_MAP = {
    # --- Hand‑written templates -------------------------------------------
    "shodan.py":      ("specific", "shodan.py.j2"),
    "geopy.py":       ("specific", "geopy.py.j2"),
    "gpt4all.py":     ("specific", "gpt4all.py.j2"),
    "llama_cpp.py": ("specific", "llama_cpp.py.j2"),

    # --- Generic REST examples -------------------------------------------
    "alienvault_otx.py": ("rest", {
        "name": "AlienVault OTX",
        "url": "https://otx.alienvault.com/api/v1/indicators/IPv4",  # arg appended
        "query_param": "",  # empty → arg placed after last slash
        "headers": {"X-OTX-API-KEY": os.getenv("OTX_KEY", "")},
    }),
    "ipinfo.py": ("rest", {
        "name": "IPinfo",
        "url": "https://ipinfo.io",          # we will build /<arg>/json
        "query_param": "",                    # empty path style
        "headers": {"Authorization": f"Bearer {os.getenv('IPINFO_TOKEN','')}"},
    }),

    # --- Generic CLI examples --------------------------------------------
    "amass.py": ("cli", {
        "name": "Amass",
        "exec_name": "amass",
        "arg_pattern": "enum -d {arg} -o -",
        "cmd_builder": "amass enum -d {arg} -o -", # This is the string literal value
    }),
    "nmap.py": ("cli", {
        "name": "Nmap",
        "exec_name": "nmap",
        "arg_pattern": "-A {arg}",
        "cmd_builder": "nmap -A {arg}",
    }),
    # ---------------------------------------------------------------------
    # Add more entries here as you template more tools
    # ---------------------------------------------------------------------
}

# Helper to choose template content

def render_template(strategy: str, cfg):
    if strategy == "specific":
        return env.get_template(cfg).render()
    if strategy == "rest":
        return env.get_template("_generic_rest.py.j2").render(**cfg)
    if strategy == "cli":
        return env.get_template("_generic_cli.py.j2").render(**cfg)
    raise ValueError(f"Unknown strategy {strategy}")


def integrate():
    """Render templates and overwrite matching stub files."""
    # Ensure 'def integrate():' starts at column 0
    # Ensure this block is correctly indented by 4 spaces
    if not TEMPLATES_DIR.exists():
        # This raise is indented by 8 spaces
        raise RuntimeError("templates/ directory not found")

    # Ensure this block is correctly indented by 4 spaces
    if not TOOLS_DIR.exists():
        # This raise is indented by 8 spaces
        raise RuntimeError(f"Tools directory not found: {TOOLS_DIR}")
        # REMOVED: The misplaced print statement was here

    # ADDED: Correctly placed print statement before the loop, indented by 4 spaces
    print(f"Starting integration process into directory: {TOOLS_DIR.resolve()}")

    # Ensure this for loop is correctly indented by 4 spaces
    for stub_path in TOOLS_DIR.glob("*.py"):
        # Lines inside the for loop body are indented by 8 spaces
        print(f"\nProcessing file: {stub_path}")

        mapping = TEMPLATE_MAP.get(stub_path.name)

        # Ensure this if block is correctly indented by 8 spaces
        if not mapping:
            # Lines inside the if block are indented by 12 spaces
            print(f"  No template mapping found for {stub_path.name}. Skipping.") # UNCOMMENTED
            continue # Ensure this continue is indented by 12 spaces

        # These lines are outside the 'if not mapping:' block,
        # at the same indentation level as the 'if' keyword (8 spaces)
        strategy, cfg = mapping
        rendered_code = render_template(strategy, cfg) # rendered_code is defined here

        # Debug prints inside the loop, indented by 8 spaces
        print(f"  Template strategy: {strategy}")
        if strategy == "cli": # Indented by 8 spaces
            print(f"  CLI Config: name='{cfg.get('name')}', exec_name='{cfg.get('exec_name')}', cmd_builder='{cfg.get('cmd_builder')}'") # Indented by 12 spaces
        elif strategy == "specific": # Indented by 8 spaces
             print(f"  Specific Template: {cfg}") # Indented by 12 spaces

        print(f"  Attempting to write to: {stub_path.resolve()}") # Indented by 8 spaces

        # The try block starts here, indented by 8 spaces
        try:
            # Lines inside the try block are indented by 12 spaces
            stub_path.write_text(rendered_code, encoding="utf-8")
            print(f"  Successfully wrote to {stub_path.name}.")
            written_content = stub_path.read_text(encoding="utf-8")
            print(f"  Verified content length: {len(written_content)} bytes.")
            # Optional print lines would be indented by 12 spaces
            # print("  First 5 lines of written content:")
            # for i, line in enumerate(written_content.splitlines()[:5]): # Indented by 12 spaces
            #     print(f"    {i+1}: {line}") # Indented by 16 spaces

        # Except blocks are at the same indentation level as the try block (8 spaces)
        except PermissionError:
            # Lines inside except block are indented by 12 spaces
            print(f"  ERROR: Permission denied when writing to {stub_path.name}. Check file/folder permissions!")
        except Exception as e: # This catches the NameError, indented by 8 spaces
            # Lines inside except block are indented by 12 spaces
            print(f"  ERROR: An unexpected error occurred when writing to {stub_path.name}: {e}")

        # Final print inside the loop, indented by 8 spaces
        print(f"Integrated {stub_path.name} via {strategy}")


# Ensure 'if __name__ == "__main__":' starts at column 0
if __name__ == "__main__":
    # Line inside the if block, indented by 4 spaces
    integrate()
    # REMOVED: Stray 'S' was here