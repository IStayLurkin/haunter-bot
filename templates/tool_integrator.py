import os
from jinja2 import Environment, FileSystemLoader

# tool_integrator.py
# Automates filling out stub modules in tools/ by rendering Jinja2 templates.

# Directory paths
TOOLS_DIR = os.path.join(os.getcwd(), "tools")
TEMPLATES_DIR = os.path.join(os.getcwd(), "templates")

# Ensure templates directory exists
if not os.path.isdir(TEMPLATES_DIR):
    os.makedirs(TEMPLATES_DIR)
    print(f"Created templates directory at {TEMPLATES_DIR}. Place your .j2 files there.")

# Initialize Jinja2 environment
env = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR),
    trim_blocks=True,
    lstrip_blocks=True,
)

def integrate():
    """
    For each stub in tools/, if a matching template exists in templates/,
    render it and overwrite the stub with integrated code.
    """
    templates = set(os.listdir(TEMPLATES_DIR))
    for stub in os.listdir(TOOLS_DIR):
        if not stub.endswith('.py'):
            continue
        template_name = f"{stub}.j2"
        template_path = os.path.join(TEMPLATES_DIR, template_name)
        if template_name not in templates:
            continue
        # Render template
        template = env.get_template(template_name)
        # You can pass additional context here, e.g., API key var names
        rendered = template.render()
        # Write back to stub file
        stub_path = os.path.join(TOOLS_DIR, stub)
        with open(stub_path, 'w', encoding='utf-8') as f:
            f.write(rendered)
        print(f"Integrated {stub} using {template_name}")

if __name__ == '__main__':
    integrate()
