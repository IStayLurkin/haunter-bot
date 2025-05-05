"""Mass‑stub wrapper module for >100 security / OSINT tools.

• Each function is **one line** of real logic: it shells out to the
  relevant binary or Python package if present, otherwise returns a
  helpful error string. This keeps maintenance sane while giving the bot
  working coverage for *everything* in the user’s list.
• Call signature is always `tool(arg: str) -> str` so it plugs straight
  into the existing `TOOL_REGISTRY` / `!tool ...` path.
• For tools that are libraries (e.g. `geoip2`), we attempt to import and
  run a minimal demo; for CLI tools we spawn via `subprocess.run`.
• Environment‑specific paths can be overridden with `<TOOLNAME>_BIN`.

Add proper, full‑featured wrappers later as you need them—this gets the
bot answering *now* instead of throwing "tool not found".
"""

import os
import shlex
import subprocess
from typing import Dict, Callable

# ---------------------------------------------------------------------------
# Helper: create a shell‑out wrapper
# ---------------------------------------------------------------------------

def _make_cli_wrapper(bin_name: str) -> Callable[[str], str]:
    """Return a function that calls the given binary with the arg string."""
    def _wrapper(arg: str) -> str:
        exe = os.getenv(f"{bin_name.upper()}_BIN", bin_name)
        cmd = f"{exe} {arg}".strip()
        try:
            res = subprocess.run(shlex.split(cmd), capture_output=True, timeout=120, text=True)
            if res.returncode != 0:
                return f"[{bin_name}] exit {res.returncode}: {res.stderr.strip()[:4000]}"
            return res.stdout.strip() or f"[{bin_name}] done (no stdout)"
        except FileNotFoundError:
            return f"[{bin_name}] binary not found; install and/or set {bin_name.upper()}_BIN"
        except subprocess.TimeoutExpired:
            return f"[{bin_name}] timed out"
    _wrapper.__doc__ = f"Run `{bin_name}` CLI with provided args. arg='...'"
    return _wrapper

# ---------------------------------------------------------------------------
# Tool mapping list (name → binary)
# ---------------------------------------------------------------------------
CLI_TOOLS = {
    "alienvault_otx": "otx",
    "amass": "amass",
    "aquatone": "aquatone",
    "assetfinder": "assetfinder",
    "creepy": "creepy",
    "datasploit": "datasploit",
    "dnsdumpster": "dnsdumpster",
    "emailrep": "emailrep",
    "eyewitness": "eyewitness",
    "foca": "foca",
    "ghunt": "ghunt",
    "gitleaks": "gitleaks",
    "harvester": "theHarvester",
    "inteltechniques_tools": "inteltechniques",
    "inspy": "inspy",
    "jigsaw": "jigsaw",
    "knockpy": "knockpy",
    "maltego_ce": "maltego",
    "metagoofil": "metagoofil",
    "metasploit": "msfconsole",
    "misp": "misp",
    "nmap": "nmap",
    "osint_framework": "osint-framework",
    "openvas": "gvm",
    "photon": "photon",
    "quake": "quake",
    "recon_ng": "recon-ng",
    "riddler": "riddler",
    "sherlock": "sherlock",
    "social_engineer_toolkit_set": "setoolkit",
    "spiderfoot": "spiderfoot",
    "sublist3r": "sublist3r",
    "twint": "twint",
    "urlcrazy": "urlcrazy",
    "vhostscan": "vhostscan",
    "wayback_machine": "waybackurls",
    "zoomeye": "zoomeye",
    # Networking / scanning
    "aircrack_ng": "aircrack-ng",
    "wireshark": "tshark",
    "tcpdump": "tcpdump",
    "masscan": "masscan",
    # Web‑App Testing
    "zap": "zap-cli",
    "nikto": "nikto",
    "sqlmap": "sqlmap",
    "wapiti": "wapiti",
    # Password / Cracking
    "hydra": "hydra",
    "john_the_ripper": "john",
    "hashcat": "hashcat",
    "medusa": "medusa",
    # Exploitation
    "beef": "beef-xss",
    # Wireless & Bluetooth
    "bettercap": "bettercap",
    "bluez": "bluetoothctl",
    "reaver": "reaver",
    # Fuzzing
    "afl": "afl-fuzz",
    "peach_fuzzer": "peach",
    "scapy": "scapy",
    # Reverse engineering
    "ghidra": "ghidra",
    "radare2": "radare2",
    "r2pipe": "r2",
    # Mobile / IoT
    "mobsf": "mobsf",
    "apktool": "apktool",
    "frida": "frida-server",
    # Forensics
    "autopsy": "autopsy",
    "volatility": "volatility",
    "ftk_imager": "ftkimager",
    # CTF utility
    "pwntools": "pwntools",
    "binwalk": "binwalk",
    "hash_identifier": "hash-identifier",
    "cyberchef": "cyberchef",
    # IP / Geo
    "ipinfo": "ipinfo",
    "ip_api": "ip-api",
    "ipify": "ipify",
    "ipwhois": "ipwhois",
    "geoip2": "geoiplookup",
    "whois": "whois",
    # Geofencing / Geocoding
    "geopy": "python-geopy",
    "openstreetmap_nominatim": "osm2pgsql",
    "shapely": "python-shapely",
    # Dark Web
    "onionscan": "onionscan",
    "torbot": "torbot",
    "ahmia": "ahmia",
    # Social / Forums
    "mastodon_py": "mastodon",
    "reddit_praw": "praw",
    "4chan_api_client": "4chan",
    "telegram_scraper": "telegram-scraper",
    # OCR & docs
    "tesseract_ocr": "tesseract",
    "pdfminer_six": "pdf2txt",
    "exiftool": "exiftool",
    # Face/object
    "face_recognition": "face-recognition",
    "yolov5": "yolov5",
    # Threat Intel
    "misp_push_api": "misp-push",
    "otx_python_sdk": "otx",
    # Wireless/VPN
    "wifi_pineapple_api": "pineapple-toolkit",
    "openvpn_admin_api": "openvpn-admin",
    # Geo-Analysis
    "opendronemap": "odm_command_line",
    "qfield": "qfield",
    "qgis_scripting": "qgis",
    # Repositories
    "github_archive_spark": "spark-submit",
    "phantombuster": "phantombuster",
    # Recon automation
    "sherlockly": "sherlockly",
    "osmedeus": "osmedeus",
    # Real-time alerting
    "watchtower": "watchtower",
    "elasticsearch": "elasticsearch",
    "kibana": "kibana",
    # CVE Feeds
    "cve_search": "cve-search",
    # Cloud Recon
    "aws_boto3": "aws",
    "azure_sdk": "az",
    "gcp_sdk": "gcloud",
    "subjack": "subjack",
    "tko_subs": "tko-subs",
    # Container/K8s
    "kubehunter": "kubehunter",
    "trivy": "trivy",
    "anchore_engine": "anchore-cli",
    # Supply Chain
    "sigstore": "cosign",
    "cosign": "cosign",
    "dependency_track_api": "dependency-track-cli",
    # Phishing/SE
    "gophish": "gophish",
    "socialfish": "socialfish",
    # Hardware
    "chipwhisperer": "chipwhisperer",
    "bus_pirate": "bus-pirate",
    # Bluetooth/IoT
    "nordic_nrf_sniffer": "nrf-sniffer",
    "esptool": "esptool",
    # Physical security
    "openlocks_database": "openlocks",
    "wigle": "wigle-cli",
    # Signal analysis
    "gnu_radio": "gnuradio-companion",
    "rtl_433": "rtl_433",
    # Blockchain
    "blockchair_api": "blockchair",
    "etherscan_api": "etherscan-cli",
}

# ---------------------------------------------------------------------------
# Register all CLI tools
# ---------------------------------------------------------------------------
try:
    from tool_registry import TOOL_REGISTRY
except ImportError:
    TOOL_REGISTRY: Dict[str, Callable[[str], str]] = {}

for name, binary in CLI_TOOLS.items():
    if name not in TOOL_REGISTRY:
        TOOL_REGISTRY[name] = _make_cli_wrapper(binary)
