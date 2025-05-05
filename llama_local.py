import asyncio
import os

MODEL_PATH = os.getenv("GPT4ALL_MODEL_PATH", "Meta-Llama-3-8B-Instruct")
BIN_PATH = r"C:\Users\btayl\llama.cpp\build\bin\Release\llama-simple-chat.exe"
SYSTEM_PROMPT = "You are an assistant that answers clearly and helpfully."

async def query_llama_local(prompt: str) -> str:
    try:
        process = await asyncio.create_subprocess_exec(
            BIN_PATH, "-m", MODEL_PATH,
            "--system", SYSTEM_PROMPT,
            "-p", prompt,
            "--ctx-size", "2048",
            "--n-gpu-layers", "100",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        try:
            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=30)
        except asyncio.TimeoutError:
            process.kill()
            return "[Timeout] LLaMA took too long to respond."

        if process.returncode == 0:
            output = stdout.decode().strip()
            return output.split("\n")[-1].strip()
        else:
            return f"[LLaMA Error] {stderr.decode().strip()}"

    except Exception as e:
        return f"[Subprocess Crash] {str(e)}"
