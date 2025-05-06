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
        log.info(f"🧠 Loading GPT4All model from: {model_path}")
        log.info(f"[LLMManager] Attempting to load GPT4All model from path: {self.model_path}")
        try:
            # Try by name first (hosted or cache), allow download
            self.model = GPT4All(self.model_path, allow_download=True)
        except FileNotFoundError:
            log.warning(f"[LLMManager] Model not found in cache, falling back to local file path {model_path}")
            try:
                self.model = GPT4All(self.model_path, allow_download=False)
            except Exception as e:
                log.error(f"❌ Failed to load GPT4All model: {e}", exc_info=True)
                self.model = None
        except Exception as e:
            log.error(f"❌ Failed to load GPT4All model: {e}", exc_info=True)
            self.model = None

    def generate_text(self, prompt, **kwargs):
        if self.model is None:
            log.warning("⚠️ LLM not loaded, falling back to llama_local")
            return "⚠️ Fallback: " + query_llama_local(prompt)
        try:
            usable_tokens = CONTEXT_LIMIT - kwargs.get("max_tokens", 256)
            trimmed_prompt = truncate_to_token_limit(prompt, usable_tokens)
            log.debug(f"[Prompt] {trimmed_prompt}")

            # Map kwargs to GPT4All.generate params
            gen_kwargs = {}
            # Map max_tokens to n_predict
            if 'max_tokens' in kwargs:
                gen_kwargs['n_predict'] = kwargs.pop('max_tokens')
            # Map temperature to temp
            if 'temperature' in kwargs:
                gen_kwargs['temp'] = kwargs.pop('temperature')
            # Map other parameters if needed (top_p, stop_sequences)
            if 'top_p' in kwargs:
                gen_kwargs['top_p'] = kwargs.pop('top_p')
            if 'stop_sequences' in kwargs:
                gen_kwargs['stop'] = kwargs.pop('stop_sequences')

            def _generate():
                return self.model.generate(trimmed_prompt, **gen_kwargs)

            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(_generate)
                result = future.result(timeout=60)  # a minute timeout
                log.debug(f"[Response] {result}")
                return result.strip()

        except concurrent.futures.TimeoutError:
            log.error("🔥 GPT4All generation timed out after 60 seconds.")
            return "🔥 Timeout: " + query_llama_local(prompt)
        except Exception as e:
            trace = traceback.format_exc()
            log.error(f"🔥 Generation error: {e}\n{trace}")
            return "🔥 Fallback: " + query_llama_local(prompt)

def get_llm():
    global _llm_instance
    if _llm_instance is None:
        # Use env var or default
        model_path = os.getenv("GPT4ALL_MODEL_PATH", "Meta-Llama-3-8B-Instruct")
        _llm_instance = LLMManager(model_path)
    return _llm_instance
