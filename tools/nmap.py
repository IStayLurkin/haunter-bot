"""Nmap wrapper (generic CLI)

Runs: nmap -A {arg}
Returns stdout (trimmed) or an error string.
"""

import subprocess, shlex

CMD_TEMPLATE = "nmap -A {arg}"

def run(arg: str) -> str:
    if not arg:
        return f"[Nmap] Empty argument."

    try:
        cmd = CMD_TEMPLATE.format(arg=arg)
        out = subprocess.check_output(
            shlex.split(cmd),
            stderr=subprocess.STDOUT,
            timeout=600  # 10‑minute ceiling for long scans
        )
        return out.decode()[:4000] or f"[Nmap] No output"
    except subprocess.TimeoutExpired:
        return f"[Nmap] Timed‑out (>10 min). Try a smaller scope."
    except subprocess.CalledProcessError as e:
        return f"[Nmap] {e.output.decode()}"
    except Exception as e:
        return f"[Nmap] {e}"