import os
from llama_cpp import Llama
import logging

logger = logging.getLogger(__name__)

TOOL_NAME = "LlamaCPP"
MODEL_PATH = os.getenv("LLAMACPP_MODEL_PATH") # Use a different env var name

llm_model = None
if not MODEL_PATH:
     logger.error("LLAMACPP_MODEL_PATH environment variable not set.")
else:
    try:
        # Load the model
        llm_model = Llama(
            model_path=MODEL_PATH,
            n_ctx=4096, # Context window size (match model capability)
            n_gpu_layers=-1, # Uncomment to offload all layers to GPU (if CUDA built)
            verbose=False # Reduce verbosity
        )
        logger.info(f"Successfully loaded LlamaCPP model from {MODEL_PATH}")
    except Exception as e:
        logger.error(f"Failed to load LlamaCPP model from {MODEL_PATH}: {e}")


def run(arg: str) -> str:
    if not llm_model:
        return f"[{TOOL_NAME}] Model not loaded. Please set LLAMACPP_MODEL_PATH correctly."

    if not arg or not arg.strip():
        return f"[{TOOL_NAME}] Please provide a prompt."

    try:
        # Example for a simple completion
        output = llm_model.create_completion(
            arg,
            max_tokens=200,
            temperature=0.7,
            stop=["\n", "User:"] # Stop sequences
        )
        response = output["choices"][0]["text"]

        # Example for chat completion (if model supports it)
        # messages = [{"role": "user", "content": arg}] # Need to manage history for conversation
        # chat_output = llm_model.create_chat_completion(
        #    messages,
        #    max_tokens=200,
        #    temperature=0.7,
        # )
        # response = chat_output["choices"][0]["message"]["content"]


        MAX_RESPONSE_LENGTH = 1900
        if len(response) > MAX_RESPONSE_LENGTH:
            response = response[:MAX_RESPONSE_LENGTH] + "..."

        return response.strip() or f"[{TOOL_NAME}] No response generated."

    except Exception as e:
         logger.error(f"Error during LlamaCPP generation: {e}")
         return f"[{TOOL_NAME}] An error occurred during generation: {e}"
