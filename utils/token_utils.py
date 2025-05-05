# utils/token_utils.py
import tiktoken

def truncate_to_token_limit(text: str, max_tokens: int, model: str = "gpt2") -> str:
    try:
        enc = tiktoken.encoding_for_model(model)
    except Exception:
        enc = tiktoken.get_encoding("cl100k_base")

    tokens = enc.encode(text)
    if len(tokens) <= max_tokens:
        return text
    return enc.decode(tokens[-max_tokens:])