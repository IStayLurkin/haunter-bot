import argparse
import logging
import sys
import os

# Adjust path to import from src directory
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(current_dir, 'src'))

# Now import modules from src
try:
    from utils import load_config, setup_logging
    from llm_interface import get_llm_interface, LLMInterface
    from memory import ChatMemory
    from cli_interface import run_cli_loop
    from discord_bot import run_discord_bot
except ImportError as e:
     print(f"Error importing necessary modules: {e}")
     print("Please ensure the script is run from the project root directory or that the 'src' directory is in the Python path.")
     sys.exit(1)


def main():
    """Main entry point for the Offline LLM Bot."""
    setup_logging() # Configure logging first

    parser = argparse.ArgumentParser(
        description="Offline LLM Bot with Tool Usage and Discord Integration.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '--config',
        type=str,
        default='config/config.yaml', # Default path relative to project root
        help='Path to the configuration file (YAML).'
    )
    parser.add_argument(
        '--interface',
        type=str,
        choices=['cli', 'discord'],
        default=None,
        help='Force a specific interface (cli or discord), overriding the config file setting.'
    )
    args = parser.parse_args()

    try:
        # --- Load Configuration ---
        # Ensure the config path is treated relative to the script's location (project root)
        config_path = os.path.join(current_dir, args.config)
        if not os.path.exists(config_path):
             # Try path relative to CWD if not found relative to script
             config_path = args.config
             if not os.path.exists(config_path):
                   logging.error(f"Configuration file not found at '{args.config}' (tried relative to script and CWD).")
                   print(f"ERROR: Configuration file not found at '{args.config}'")
                   sys.exit(1)

        # Pass the absolute path to load_config
        config = load_config(config_path=config_path)

        # --- Initialize LLM ---
        logging.info("Initializing LLM...")
        llm = get_llm_interface(config)
        logging.info(f"LLM Initialized: Type={config['llm']['type']}, Model={llm.get_model_name()}")

        # --- Determine Interface ---
        # Command-line argument takes precedence over config file
        if args.interface == 'cli':
            run_discord_mode = False
            logging.info("CLI interface forced via command line argument.")
        elif args.interface == 'discord':
            run_discord_mode = True
            logging.info("Discord interface forced via command line argument.")
        else:
            # Use config file setting if no command-line override
            run_discord_mode = config.get('discord', {}).get('enabled', False)
            logging.info(f"Interface selected based on config: {'Discord' if run_discord_mode else 'CLI'}")


        # --- Run Selected Interface ---
        if run_discord_mode:
            # Discord bot manages its own memory instances per channel/DM
            run_discord_bot(config, llm)
        else:
            # CLI uses a single, shared memory instance
            logging.info("Initializing shared memory for CLI mode...")
            memory = ChatMemory(config)
            run_cli_loop(config, llm, memory)

    except (ValueError, ImportError, FileNotFoundError, ConnectionError) as e:
        logging.error(f"Initialization or runtime error: {e}", exc_info=True) # Log traceback for these
        print(f"\nERROR: {e}")
        print("Please check configuration, model paths, dependencies, and ensure required services (like Ollama) are running.")
        sys.exit(1)
    except KeyboardInterrupt:
         print("\nExiting bot...")
         logging.info("Shutdown requested via KeyboardInterrupt.")
         sys.exit(0)
    except Exception as e:
        # Catch any other unexpected errors
        logging.critical(f"An unexpected critical error occurred: {e}", exc_info=True)
        print(f"\nCRITICAL ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
