"""Masscan wrapper (generic CLI)

Runs: masscan -p80 {arg}
Returns stdout (trimmed) or an error string.
"""

import subprocess, shlex

CMD_TEMPLATE = "masscan -p80 {arg}"

def run(arg: str) -> str:
    if not arg:
        return f"[Masscan] Empty argument."

    try:
        cmd = CMD_TEMPLATE.format(arg=arg)
        out = subprocess.check_output(
            shlex.split(cmd),
            stderr=subprocess.STDOUT,
            timeout=600  # 10‑minute ceiling for long scans
        )
        return out.decode()[:4000] or f"[Masscan] No output"
    except subprocess.TimeoutExpired:
        return f"[Masscan] Timed‑out (>10 min). Try a smaller scope."
    except subprocess.CalledProcessError as e:
        return f"[Masscan] {e.output.decode()}"
    except Exception as e:
        return f"[Masscan] {e}"