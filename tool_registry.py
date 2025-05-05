"""
Dynamic loader for all tool modules in the `tools` package.
Populates the `TOOLS` dict mapping tool names to their callable implementations.
"""
import importlib
import pkgutil

TOOLS: dict[str, callable] = {}

def load_tools() -> None:
    """Discover and import all modules in the tools package."""
    try:
        import tools
        tools_path = tools.__path__
    except ImportError:
        return

    for finder, name, ispkg in pkgutil.iter_modules(tools_path):
        if ispkg:
            continue
        try:
            module = importlib.import_module(f"tools.{name}")
        except Exception:
            continue
        # If module defines a run(arg) function, register it
        if hasattr(module, "run") and callable(module.run):
            TOOLS[name] = module.run

# Load all CLI-based tools
load_tools()

# Explicitly import the image suite so it self-registers
try:
    import tools.tools_image_suite  # noqa: F401
except ImportError:
    pass
