
import logging
from gpt4all import GPT4All
from llama_local import query_llama_local  # fallback
import os
from utils.token_utils import truncate_to_token_limit
from config.constants import CONTEXT_LIMIT
import concurrent.futures
import traceback

log = logging.getLogger("llm_manager")
_llm_instance = None

class LLMManager:
    def __init__(self, model_path: str):
        self.model = None
        self.model_path = model_path

        # Step 1: Try hosted model (and download if missing)
        log.info(f"[LLMManager] Trying hosted model '{model_path}' (allowing download)…")
        try:
            # allow_download=True will fetch the .gguf into your cache if not present
            self.model = GPT4All(model_path, allow_download=True)
            log.info(f"[LLMManager] Loaded hosted model '{model_path}'")
            return
        except Exception as e:
            log.error(f"[LLMManager] Hosted load failed: {e}", exc_info=True)

        # Step 2: Fallback to your local .gguf file
        local = r"F:/Projects/haun/models/Meta-Llama-3-8B-Instruct.Q4_0.gguf"
        log.info(f"[LLMManager] Falling back to local file '{local}'…")
        try:
            self.model = GPT4All(local, allow_download=False)
            log.info(f"[LLMManager] Loaded local model at '{local}'")
        except Exception as e:
            log.error(f"[LLMManager] Local load failed: {e}", exc_info=True)
            self.model = None

    def generate_text(self, prompt, **kwargs):
        if self.model is None:
            log.warning("⚠️ LLM not loaded, falling back to llama_local")
            return "⚠️ Fallback: " + query_llama_local(prompt)

        try:
            usable_tokens = CONTEXT_LIMIT - kwargs.get("max_tokens", 256)
            trimmed_prompt = truncate_to_token_limit(prompt, usable_tokens)
            log.debug(f"[Prompt] {trimmed_prompt}")

            def _generate():
                return self.model.generate(trimmed_prompt, **kwargs)

            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(_generate)
                result = future.result(timeout=15)
                log.debug(f"[Response] {result}")
                return result.strip()

        except concurrent.futures.TimeoutError:
            log.error("🔥 GPT4All generation timed out after 15 seconds.")
            return "🔥 Timeout: " + query_llama_local(prompt)
        except Exception as e:
            trace = traceback.format_exc()
            log.error(f"🔥 GPT4All generation error: {e}\n{trace}")
            return "🔥 Fallback: " + query_llama_local(prompt)

def get_llm():
    global _llm_instance
    if _llm_instance is None:
        # Force using the hosted model name; ignore any ENV var
        model_path = "Meta-Llama-3-8B-Instruct"
        log.info(f"[LLMManager] Forcing model name (ignoring ENV): {model_path}")
        _llm_instance = LLMManager(model_path)
    return _llm_instance