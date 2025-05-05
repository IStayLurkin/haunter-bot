"""Amass wrapper (generic CLI)

Runs: amass enum -d {arg} -o -
Returns stdout (trimmed) or an error string.
"""

import subprocess, shlex

CMD_TEMPLATE = "amass enum -d {arg} -o -"

def run(arg: str) -> str:
    if not arg:
        return f"[Amass] Empty argument."

    try:
        cmd = CMD_TEMPLATE.format(arg=arg)
        out = subprocess.check_output(
            shlex.split(cmd),
            stderr=subprocess.STDOUT,
            timeout=600  # 10‑minute ceiling for long scans
        )
        return out.decode()[:4000] or f"[Amass] No output"
    except subprocess.TimeoutExpired:
        return f"[Amass] Timed‑out (>10 min). Try a smaller scope."
    except subprocess.CalledProcessError as e:
        return f"[Amass] {e.output.decode()}"
    except Exception as e:
        return f"[Amass] {e}"