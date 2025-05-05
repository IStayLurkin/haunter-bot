"""IPinfo wrapper (generic REST)

Calls: https://ipinfo.io/{arg}
Headers: {'Authorization': 'Bearer '}
"""

import json, requests

URL          = "https://ipinfo.io"
QUERY_PARAM  = ""
HEADERS      = {"Authorization": "Bearer "}

def run(arg: str) -> str:
    """Query the REST endpoint for *arg* and return prettified JSON."""
    if not arg:
        return f"[IPinfo] Empty argument."

    # Build full URL (path vs query style)
    full_url = f"{URL}/{arg}" if not QUERY_PARAM else f"{URL}?{QUERY_PARAM}={arg}"

    try:
        r = requests.get(full_url, headers=HEADERS, timeout=10)
        r.raise_for_status()
        # Truncate to 4 k chars for Discord
        return json.dumps(r.json(), indent=2)[:4000]
    except Exception as e:
        return f"[IPinfo] {e}"
