import yaml
import logging
import os
import sys

def setup_logging():
    """Configures basic logging."""
    logging.basicConfig(
        level=logging.INFO, # Set to DEBUG for more verbose output
        format='%(asctime)s - %(levelname)s - [%(module)s:%(lineno)d] - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout) # Log to console
            # Optionally add a FileHandler:
            # logging.FileHandler('bot.log', encoding='utf-8')
        ]
    )
    logging.info("Logging setup complete.")

def load_config(config_path='../config/config.yaml') -> dict:
    """
    Loads configuration from a YAML file relative to this script's location.
    Resolves relative paths for model and memory based on the project root.
    Overrides Discord token with environment variable if available.
    """
    try:
        # Determine the absolute path to the config file
        base_dir = os.path.dirname(os.path.abspath(__file__)) # Directory of utils.py (src)
        project_root = os.path.dirname(base_dir) # Project root (one level up)
        abs_config_path = os.path.join(base_dir, config_path) # Path relative to src/

        if not os.path.exists(abs_config_path):
             # Fallback: try path relative to project root if called differently
             abs_config_path_alt = os.path.join(project_root, config_path.replace('../', ''))
             if os.path.exists(abs_config_path_alt):
                 abs_config_path = abs_config_path_alt
             else:
                  raise FileNotFoundError(f"Config file not found at {abs_config_path} or {abs_config_path_alt}")


        with open(abs_config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)

        # --- Resolve relative paths ---
        # Assume paths in config are relative to the *project root*
        if 'llm' in config and 'model_path' in config['llm'] and not os.path.isabs(config['llm']['model_path']):
            config['llm']['model_path'] = os.path.join(project_root, config['llm']['model_path'])
            logging.debug(f"Resolved LLM model path: {config['llm']['model_path']}")

        if 'memory' in config and 'path' in config['memory'] and not os.path.isabs(config['memory']['path']):
            config['memory']['path'] = os.path.join(project_root, config['memory']['path'])
            logging.debug(f"Resolved memory path: {config['memory']['path']}")

        # --- Override with Environment Variables (for secrets) ---
        discord_token_env = os.environ.get('DISCORD_BOT_TOKEN')
        if discord_token_env:
            if 'discord' not in config:
                config['discord'] = {}
            config['discord']['token'] = discord_token_env
            logging.info("Using Discord token from environment variable.")
        elif config.get('discord', {}).get('token') == 'YOUR_DISCORD_BOT_TOKEN':
             logging.warning("Discord token is set to the placeholder value in config.")


        logging.info(f"Configuration loaded successfully from {abs_config_path}")
        return config

    except FileNotFoundError:
        logging.error(f"CRITICAL: Configuration file not found.")
        raise
    except yaml.YAMLError as e:
        logging.error(f"CRITICAL: Error parsing configuration file {abs_config_path}: {e}")
        raise
    except Exception as e:
        logging.error(f"CRITICAL: Failed to load or process configuration: {e}")
        raise

