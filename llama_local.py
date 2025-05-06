
import os
import subprocess

# Safely resolve the model path from ENV or fallback to default name
MODEL_PATH = os.getenv("GPT4ALL_MODEL_PATH", "Meta-Llama-3-8B-Instruct")
BIN_PATH = r"C:\Users\btayl\llama.cpp\build\bin\Release\llama-simple-chat.exe"
SYSTEM_PROMPT = "You are an assistant that answers clearly and helpfully."

def query_llama_local(prompt: str) -> str:
    try:
        result = subprocess.run(
            [BIN_PATH, "-m", MODEL_PATH, "--system", SYSTEM_PROMPT, "-p", prompt,
             "--ctx-size", "2048", "--n-gpu-layers", "100"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=90
        )
        if result.returncode == 0:
            output = result.stdout.strip()
            return output.split("\n")[-1].strip()
        else:
            return f"[LLaMA Error] {result.stderr.strip()}"
    except Exception as e:
        return f"[Subprocess Crash] {str(e)}"
