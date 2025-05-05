"""AlienVault OTX wrapper (generic REST)

Calls: https://otx.alienvault.com/api/v1/indicators/IPv4/{arg}
Headers: {'X-OTX-API-KEY': ''}
"""

import json, requests

URL          = "https://otx.alienvault.com/api/v1/indicators/IPv4"
QUERY_PARAM  = ""
HEADERS      = {"X-OTX-API-KEY": ""}

def run(arg: str) -> str:
    """Query the REST endpoint for *arg* and return prettified JSON."""
    if not arg:
        return f"[AlienVault OTX] Empty argument."

    # Build full URL (path vs query style)
    full_url = f"{URL}/{arg}" if not QUERY_PARAM else f"{URL}?{QUERY_PARAM}={arg}"

    try:
        r = requests.get(full_url, headers=HEADERS, timeout=10)
        r.raise_for_status()
        # Truncate to 4 k chars for Discord
        return json.dumps(r.json(), indent=2)[:4000]
    except Exception as e:
        return f"[AlienVault OTX] {e}"
