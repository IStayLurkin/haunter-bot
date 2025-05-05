# llm_integrator.py
from llm_manager import get_llm
import os, re

LLM = get_llm()

def slug(name): 
    return re.sub(r'[^0-9a-z]+','_', name.lower()).strip('_')

def flesh_out_stub(path):
    code = open(path,'r',encoding='utf-8').read()
    prompt = (
        "I have a Python stub:\n\n"
        f"{code}\n\n"
        "Please replace the TODO with a working integration using the standard "
        "Python API or CLI for this tool. Return only the full file."
    )
    result = LLM.generate(prompt, max_tokens=1024)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(result)

def main():
    tools_dir = "tools"
    for fn in os.listdir(tools_dir):
        if not fn.endswith(".py"):
            continue
        full = os.path.join(tools_dir, fn)
        text = open(full,'r',encoding='utf-8').read()
        if "# TODO" in text:
            print(f"Fleshing out {fn}…")
            flesh_out_stub(full)

if __name__ == "__main__":
    main()
