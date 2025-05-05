from abc import ABC, abstractmethod
import logging
import time

# --- Import LLM Libraries (handle optional dependencies) ---

# Example for llama-cpp-python
try:
    from llama_cpp import Llama
except ImportError:
    Llama = None # Placeholder if not installed
    logging.debug("llama-cpp-python not installed. LlamaCPPInterface will be unavailable.")

# Example for Ollama
try:
    import ollama
except ImportError:
    ollama = None # Placeholder if not installed
    logging.debug("ollama library not installed. OllamaInterface will be unavailable.")

# --- Abstract Base Class ---

class LLMInterface(ABC):
    """Abstract base class for different LLM interaction implementations."""

    @abstractmethod
    def __init__(self, config: dict):
        """
        Initializes the LLM interface with necessary configuration.
        Should load the model or set up the client connection.
        Args:
            config (dict): The loaded application configuration dictionary.
        """
        self.config = config
        self.model_name = "Unknown" # Default, should be overridden

    @abstractmethod
    def generate_response_with_history(self, messages: list) -> str:
        """
        Generates a response from the LLM based on a structured message history.
        Args:
            messages (list): A list of message dictionaries, typically following
                             the OpenAI format: [{'role': 'user'/'assistant'/'system', 'content': '...'}, ...]
        Returns:
            str: The generated text response from the LLM.
        """
        pass

    def get_model_name(self) -> str:
        """Returns the name or identifier of the loaded model."""
        return self.model_name

# --- Concrete Implementations ---

class LlamaCPPInterface(LLMInterface):
    """LLM Interface implementation using llama-cpp-python."""
    def __init__(self, config: dict):
        super().__init__(config)
        if not Llama:
            raise ImportError("llama-cpp-python library is required for LlamaCPPInterface but not installed.")

        llm_config = config['llm']
        model_path = llm_config.get('model_path')
        if not model_path:
             raise ValueError("Missing 'model_path' in llm config for llama_cpp type.")
        if not os.path.exists(model_path):
             raise FileNotFoundError(f"Llama model file not found at specified path: {model_path}")

        self.model_name = os.path.basename(model_path)
        n_gpu_layers = llm_config.get('n_gpu_layers', 0)
        n_ctx = llm_config.get('n_ctx', 2048)
        logging.info(f"Initializing Llama model from: {model_path}")
        logging.info(f"Using n_gpu_layers: {n_gpu_layers}, n_ctx: {n_ctx}")

        try:
            # Note: Adjust parameters like `n_batch` based on your hardware if needed
            self.model = Llama(
                model_path=model_path,
                n_gpu_layers=n_gpu_layers,
                n_ctx=n_ctx,
                verbose=logging.getLogger().level == logging.DEBUG, # Show Llama logs only if main logging is DEBUG
                # chat_format="llama-2" # Or chatml, etc. - Check model compatibility if needed
            )
            logging.info(f"Llama model '{self.model_name}' loaded successfully.")
        except Exception as e:
            logging.error(f"Failed to load Llama model from {model_path}: {e}", exc_info=True)
            raise

    def generate_response_with_history(self, messages: list) -> str:
        """Generates response using llama-cpp's chat completion endpoint."""
        logging.debug(f"Generating LlamaCPP response for {len(messages)} messages...")
        if not messages:
            logging.warning("generate_response_with_history called with empty messages list.")
            return "I need some input to respond!"

        try:
            start_time = time.time()
            # Adjust max_tokens, temperature, stop tokens etc. as needed
            response = self.model.create_chat_completion(
                messages=messages,
                max_tokens=1024, # Sensible default, adjust based on expected response length
                stop=["\nUser:", "</s>", "<|im_end|>"], # Common stop tokens, adjust per model
                temperature=0.7,
            )
            duration = time.time() - start_time
            content = response['choices'][0]['message']['content'].strip()
            # Log token usage if available
            usage = response.get('usage', {})
            prompt_tokens = usage.get('prompt_tokens', 'N/A')
            completion_tokens = usage.get('completion_tokens', 'N/A')
            logging.info(f"LlamaCPP response generated in {duration:.2f}s. Tokens: Prompt={prompt_tokens}, Completion={completion_tokens}")
            logging.debug(f"LLM Raw Response: {content[:150]}...") # Log beginning of response
            return content
        except Exception as e:
            logging.error(f"Error during llama-cpp chat completion: {e}", exc_info=True)
            return "Sorry, I encountered an internal error while generating a response."


class OllamaInterface(LLMInterface):
    """LLM Interface implementation using the Ollama library."""
    def __init__(self, config: dict):
        super().__init__(config)
        if not ollama:
            raise ImportError("ollama library is required for OllamaInterface but not installed.")

        llm_config = config['llm']
        self.host = llm_config.get('host', 'http://localhost:11434') # Default Ollama host
        self.model_name = llm_config.get('model_name')
        if not self.model_name:
             raise ValueError("Missing 'model_name' in llm config for ollama type.")

        logging.info(f"Initializing Ollama client for host: {self.host}")
        logging.info(f"Using Ollama model: {self.model_name}")

        try:
            self.client = ollama.Client(host=self.host)
            # Check connection and if model exists
            available_models = [m['name'] for m in self.client.list().get('models', [])]
            logging.debug(f"Available Ollama models: {available_models}")
            if self.model_name not in available_models:
                 logging.warning(f"Model '{self.model_name}' not found in Ollama's list. Ensure it's pulled or served.")
                 # Optionally, try to pull it? Be careful with automatic downloads.
                 # try:
                 #     logging.info(f"Attempting to pull Ollama model '{self.model_name}'...")
                 #     ollama.pull(self.model_name)
                 # except Exception as pull_e:
                 #     logging.error(f"Failed to pull Ollama model '{self.model_name}': {pull_e}")
                 #     # Decide whether to raise error or continue
            logging.info(f"Ollama client connected successfully to {self.host}.")

        except Exception as e:
            logging.error(f"Failed to connect to Ollama host {self.host} or list models: {e}", exc_info=True)
            logging.error("Please ensure the Ollama server is running and accessible.")
            raise ConnectionError(f"Could not connect to Ollama at {self.host}")


    def generate_response_with_history(self, messages: list) -> str:
        """Generates response using the ollama chat endpoint."""
        logging.debug(f"Generating Ollama response for {len(messages)} messages using model '{self.model_name}'...")
        if not messages:
            logging.warning("generate_response_with_history called with empty messages list.")
            return "I need some input to respond!"

        try:
            start_time = time.time()
            # You can add options like temperature, top_p etc. here if needed
            # options = {"temperature": 0.7}
            response = self.client.chat(
                model=self.model_name,
                messages=messages,
                # options=options
            )
            duration = time.time() - start_time
            content = response['message']['content'].strip()
            # Log token usage if available
            prompt_tokens = response.get('prompt_eval_count', 'N/A')
            completion_tokens = response.get('eval_count', 'N/A')
            logging.info(f"Ollama response generated in {duration:.2f}s. Tokens: Prompt={prompt_tokens}, Completion={completion_tokens}")
            logging.debug(f"LLM Raw Response: {content[:150]}...")
            return content
        except Exception as e:
            logging.error(f"Error during Ollama chat completion: {e}", exc_info=True)
            return "Sorry, I encountered an error communicating with the Ollama service."

# --- Factory Function ---

def get_llm_interface(config: dict) -> LLMInterface:
    """
    Factory function to create an instance of the appropriate LLM interface
    based on the configuration.
    Args:
        config (dict): The loaded application configuration.
    Returns:
        LLMInterface: An instance of a concrete LLM interface class.
    Raises:
        ValueError: If the configured LLM type is unsupported or configuration is missing.
        ImportError: If the required library for the chosen type is not installed.
        FileNotFoundError: If the model file (for llama_cpp) is not found.
        ConnectionError: If connection to the LLM service (like Ollama) fails.
    """
    if 'llm' not in config or 'type' not in config['llm']:
        raise ValueError("LLM configuration ('llm' section with 'type') is missing in the config file.")

    llm_type = config['llm']['type'].lower()
    logging.info(f"Attempting to load LLM interface of type: '{llm_type}'")

    if llm_type == 'llama_cpp':
        return LlamaCPPInterface(config)
    elif llm_type == 'ollama':
        return OllamaInterface(config)
    # Add other types here:
    # elif llm_type == 'ctransformers':
    #    return CTransformersInterface(config) # Assuming you create this class
    else:
        raise ValueError(f"Unsupported LLM type specified in config: '{llm_type}'")

# --- Helper for path resolution (needed by LlamaCPPInterface) ---
import os
