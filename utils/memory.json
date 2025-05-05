import json, os

MEMORY_FILE = "data/memory.json"
memory = {}

def load_memory():
    global memory
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            memory = json.load(f)
    else:
        memory = {}

def save_memory():
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)

def add_memory(user_id, role, content):
    user_id = str(user_id)
    if user_id not in memory:
        memory[user_id] = []
    memory[user_id].append({"role": role, "content": content})
    save_memory()

def get_recent_memory(user_id, limit=20):
    return memory.get(str(user_id), [])[-limit:]
