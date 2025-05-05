"""Llama-cpp-python wrapper (specific template)

Uses the llama-cpp-python library to run a GGUF model locally.
Requires the 'llama-cpp-python' Python library and a downloaded GGUF model file.
"""

import os
from llama_cpp import Llama
import logging

# Configure logging (optional, but helpful for debugging)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOOL_NAME = "LlamaCPP"
# Read model path from environment variable
# Use a specific environment variable name for this tool
MODEL_PATH = os.getenv("LLAMACPP_MODEL_PATH")

# Define model parameters (adjust based on your model and hardware)
# n_ctx: Context window size (how much past conversation/text the model sees)
# n_gpu_layers: Number of layers to offload to GPU (-1 for all, 0 for none)
# You might need to adjust these based on your GPU VRAM or CPU.
LLM_PARAMS = {
    "n_ctx": 4096, # Common context size, check model card
    "n_gpu_layers": -1, # Try offloading to GPU if you have one and built with cuBLAS/CLBlast
    "verbose": False # Reduce verbosity during loading
}

# Load the model once when the module is imported
llm_model = None
if not MODEL_PATH:
    logger.error(f"[{TOOL_NAME}] LLAMACPP_MODEL_PATH environment variable not set.")
else:
    if not os.path.exists(MODEL_PATH):
         logger.error(f"[{TOOL_NAME}] Model file not found at {MODEL_PATH}")
    else:
        try:
            logger.info(f"[{TOOL_NAME}] Attempting to load model from {MODEL_PATH}")
            llm_model = Llama(model_path=MODEL_PATH, **LLM_PARAMS)
            logger.info(f"[{TOOL_NAME}] Successfully loaded model from {MODEL_PATH}")
        except Exception as e:
            logger.error(f"[{TOOL_NAME}] Failed to load model from {MODEL_PATH}: {e}")


def run(arg: str) -> str:
    """Generates text using the loaded LlamaCPP model based on the input prompt."""
    if not llm_model:
        return f"[{TOOL_NAME}] Model not loaded. Please set LLAMACPP_MODEL_PATH correctly and ensure the path is valid."

    if not arg or not arg.strip():
        return f"[{TOOL_NAME}] Please provide a prompt."

    try:
        logger.info(f"[{TOOL_NAME}] Generating text with prompt: {arg[:100]}...") # Log start of generation

        # Use the create_completion method for simple text generation
        # This treats the input 'arg' as the raw prompt.
        output = llm_model.create_completion(
            arg,
            max_tokens=200, # Limit response length (tokens)
            temperature=0.7, # Controls randomness (0.0 is deterministic)
            # stop=["\n", "User:"] # Optional stop sequences
        )
        response = output["choices"][0]["text"]

        # --- Alternative: Use create_chat_completion for chat-tuned models ---
        # This formats the prompt using the model's chat template.
        # You might need to manage message history outside this tool for conversations.
        # For a single turn:
        # messages = [{"role": "user", "content": arg}]
        # chat_output = llm_model.create_chat_completion(
        #    messages=messages,
        #    max_tokens=200,
        #    temperature=0.7,
        #    # stream=True # Optional: for streaming output
        # )
        # response = chat_output["choices"][0]["message"]["content"]
        # --- End Alternative ---

        logger.info(f"[{TOOL_NAME}] Generation complete. Raw response length: {len(response)}")

        # Truncate the response for Discord message limit or your own limit
        MAX_RESPONSE_LENGTH = 1900 # Keep well below Discord's 2000 char limit
        if len(response) > MAX_RESPONSE_LENGTH:
             response = response[:MAX_RESPONSE_LENGTH] + "..." # Indicate truncation

        return response.strip() or f"[{TOOL_NAME}] No response generated or response was empty."

    except Exception as e:
        logger.error(f"[{TOOL_NAME}] Error during generation: {e}")
        return f"[{TOOL_NAME}] An error occurred during generation: {e}"

# Example of how to use the tool (for testing purposes, won't run in bot)
# if __name__ == "__main__":
#     # Requires LLAMACPP_MODEL_PATH to be set in your environment
#     print(f"Testing {TOOL_NAME} tool...")
#     test_prompt = "Tell me a short story about a brave knight."
#     print(f"Running with prompt: '{test_prompt}'")
#     result = run(test_prompt)
#     print("\nResult:")
#     print(result)
#     print("\nTest complete.")