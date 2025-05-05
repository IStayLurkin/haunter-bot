import os
import re

# scaffold_osint_tools.py
# -------------------------------------------------------------
# Generates *empty* stub modules for each tool in tool_names.
# Run this script whenever you add/remove names and need fresh
# stubs.  Filled‑out implementations are handled separately by
# tool_integrator.py using Jinja2 templates.

tool_names = [
    # --- Core OSINT & Recon ---
    "AlienVault OTX", "Amass", "Aquatone", "Assetfinder", "Creepy",
    "Datasploit", "DNSDumpster", "EmailRep", "EyeWitness", "FOCA",
    "GHunt", "GitLeaks", "Harvester", "IntelTechniques Tools",
    "InSpy", "Jigsaw", "Knockpy", "Maltego CE", "Metagoofil",
    "Metasploit", "MISP", "Nmap", "OSINT Framework", "OpenVAS",
    "Photon", "Quake", "Recon-ng", "Riddler", "Sherlock",
    "Social-Engineer Toolkit (SET)", "SpiderFoot", "Sublist3r",
    "Twint", "URLCrazy", "VHostScan", "Wayback Machine", "ZoomEye",

    # --- Networking / Scanning ---
    "Aircrack-ng", "Wireshark", "tcpdump", "Masscan",

    # --- Web‑App Testing ---
    "ZAP", "Nikto", "sqlmap", "Wapiti",

    # --- Password / Cracking ---
    "Hydra", "John the Ripper", "Hashcat", "Medusa",

    # --- Exploitation Frameworks ---
    "BeEF",

    # --- Wireless & Bluetooth ---
    "Bettercap", "BlueZ", "Reaver",

    # --- Fuzzing / Protocol ---
    "AFL", "Peach Fuzzer", "Scapy",

    # --- Reverse Engineering & Binary Analysis ---
    "Ghidra", "Radare2", "r2pipe",

    # --- Mobile / IoT Security ---
    "MobSF", "APKTool", "Frida",

    # --- Forensics & Memory ---
    "Autopsy", "Volatility", "FTK Imager",

    # --- CTF & Utility ---
    "Pwntools", "Binwalk", "Hash-identifier", "CyberChef",

    # --- IP / Geo Lookup ---
    "IPinfo", "ip-api", "Ipify", "ipwhois", "GeoIP2", "Whois",

    # --- Geofencing / Geocoding ---
    "GeoPy", "OpenStreetMap Nominatim", "Shapely",

    # --- Image Search & Generation ---
    "Google Images Search", "DuckDuckGo Images",
    "Yandex Reverse Image Search", "TinEye Reverse Image Search",
    "Stable Diffusion",

    # --- Voice / Speech ---
    "Mozilla DeepSpeech", "OpenAI Whisper",
    "CMU Sphinx", "Kaldi",

    # --- CCTV / Open‑Cam Discovery ---
    "Insecam", "Greyhat Warfare", "ONVIF Device Manager",
    "RTSP Player", "ZMap",

    # --- LLM Frameworks ---
    "llama_cpp", "GPT4All", "Hugging Face Transformers", "LangChain",
    "LlamaIndex", "OpenLLM", "BLOOM", "Mistral", "GPT-J",
    "EleutherAI GPT-Neo", "EleutherAI GPT-NeoX", "Pythia", "Falcon",
    "OPT", "FLAN-T5",

    # --- Dark‑Web / Tor Recon ---
    "OnionScan", "TorBot", "Ahmia",

    # --- Social / Forum Mining ---
    "Mastodon.py", "Reddit PRAW", "4chan API Client",
    "Telegram Scraper",

    # --- OCR & Document Extraction ---
    "Tesseract OCR", "pdfminer.six", "ExifTool",

    # --- Face / Object Recognition ---
    "face_recognition", "YOLOv5",

    # --- Threat Intel Feeds ---
    "MISP Push API", "OTX Python SDK",

    # --- Wireless & VPN Analysis ---
    "WiFi Pineapple API", "OpenVPN-Admin-API",

    # --- Geo‑Analysis / Mapping ---
    "OpenDroneMap", "QField", "QGIS Scripting",

    # --- Code & Artifact Repositories ---
    "GitHub Archive Spark", "PhantomBuster",

    # --- Recon Automation / Workflow ---
    "Sherlockly", "Osmedeus",

    # --- Real‑Time Alerting ---
    "Watchtower", "Elasticsearch", "Kibana",

    # --- CVE / Vuln Feeds ---
    "CVE-Search",

    # --- Cloud Recon ---
    "AWS Boto3", "Azure SDK", "GCP SDK", "subjack", "tko-subs",

    # --- Container / K8s Inspection ---
    "KubeHunter", "Trivy", "Anchore Engine",

    # --- Supply‑Chain / Artifact Tracking ---
    "Sigstore", "Cosign", "Dependency-Track API",

    # --- Phishing / SE Kits ---
    "GoPhish", "SocialFish",

    # --- Side‑Channel / Hardware ---
    "ChipWhisperer", "Bus Pirate",

    # --- Bluetooth & IoT ---
    "Nordic nRF Sniffer", "ESPTool",

    # --- Physical Security Recon ---
    "OpenLocks Database", "WiGLE",

    # --- Audio / Signal Analysis ---
    "GNU Radio", "rtl_433",

    # --- Crypto / Blockchain ---
    "Blockchair API", "Etherscan API",
]

def slug(name: str) -> str:
    return re.sub(r"[^0-9a-z]+", "_", name.lower()).strip("_")

def scaffold_tools() -> None:
    tools_dir = os.path.join(os.getcwd(), "tools")
    os.makedirs(tools_dir, exist_ok=True)

    for name in tool_names:
        filepath = os.path.join(tools_dir, f"{slug(name)}.py")
        if os.path.exists(filepath):
            continue
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f'"""{name} tool stub"""\n\n')
            f.write("def run(arg: str) -> str:\n")
            f.write(f'    """Run {name} against the given argument and return results."""\n')
            f.write("    # TODO: integrate actual API/CLI logic here\n")
            f.write('    return f"{name}: stub for {arg}"\n')

    print(f"Scaffolded {len(tool_names)} stubs into tools/")

if __name__ == "__main__":
    scaffold_tools()
