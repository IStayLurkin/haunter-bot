"""Image-related utility tools for Kiba/Haun bot.

All functions accept a single string argument (`arg`) and return a
string or URL that the bot will echo back.

Environment variables required for the external APIs are documented in
each docstring. Missing dependencies or keys return clear messages.
"""

import os
import json
import openai
import base64

# ---------------------------------------------------------------------------
# Google Images Search via Custom Search JSON API
# ---------------------------------------------------------------------------
def google_images_search(arg: str) -> str:
    """Google Images via Custom Search JSON API.

    Requires:
      • GOOGLE_API_KEY
      • GOOGLE_CSE_ID  (Image-only Custom Search Engine ID)

    Usage: !tool google_images_search "keyword"
    Returns first image URL.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    cse_id  = os.getenv("GOOGLE_CSE_ID")
    if not api_key or not cse_id:
        return "[google_images_search] set GOOGLE_API_KEY + GOOGLE_CSE_ID in .env"
    try:
        from googleapiclient.discovery import build
    except ImportError:
        return "[google_images_search] pip install google-api-python-client"

    service = build(
        "customsearch",
        "v1",
        developerKey=api_key,
        cache_discovery=False
    )

    try:
        res = service.cse().list(
            q=arg,
            cx=cse_id,
            searchType="image",
            num=1
        ).execute()
    except Exception as e:
        return f"[google_images_search] API error: {e}"

    items = res.get("items", [])
    if not items:
        return "[google_images_search] no results"
    return items[0].get("link", "")


# ---------------------------------------------------------------------------
# DuckDuckGo Images via duckduckgo_search
# ---------------------------------------------------------------------------
def duckduckgo_images(arg: str) -> str:
    """DuckDuckGo image search (no API key).

    Usage: !tool duckduckgo_images "keyword"
    Returns first image URL.
    """
    try:
        from duckduckgo_search import DDGS
    except ImportError:
        return "[duckduckgo_images] pip install duckduckgo_search"
    with DDGS() as ddgs:
        results = [r.get("image", "") for r in ddgs.images(arg, max_results=1)]
    if not results or not results[0]:
        return "[duckduckgo_images] no results"
    return results[0]


# ---------------------------------------------------------------------------
# Yandex Reverse Image Search
# ---------------------------------------------------------------------------
def yandex_reverse_image_search(arg: str) -> str:
    """Yandex reverse image search (HTML scrape).

    Arg may be URL or local file path. Returns best-guess page URL.
    Requires: pip install requests bs4
    """
    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError:
        return "[yandex_reverse_image_search] pip install requests bs4"
    session = requests.Session()
    upload_url = "https://yandex.com/images-search"
    page = session.get(upload_url, timeout=15)
    soup = BeautifulSoup(page.text, "html.parser")
    fuid = soup.find("input", {"name": "fuid"})
    if not fuid:
        return "[yandex_reverse_image_search] layout change"
    files = {}
    if arg.startswith("http"):
        files["img_url"] = (None, arg)
    else:
        try:
            files["upfile"] = (os.path.basename(arg), open(arg, "rb"), "image/jpeg")
        except FileNotFoundError:
            return "[yandex_reverse_image_search] file not found"
    resp = session.post(
        upload_url,
        params={"rpt": "imageview", "format": "json", "request": "{}"},
        files=files,
        timeout=30,
    )
    if resp.status_code != 200:
        return f"[yandex_reverse_image_search] HTTP {resp.status_code}"
    data = resp.json()
    try:
        url = "https://yandex.com" + data["blocks"][0]["params"]["url"]
    except Exception:
        return "[yandex_reverse_image_search] parsing error"
    return url


# ---------------------------------------------------------------------------
# TinEye Reverse Image Search via pytineye
# ---------------------------------------------------------------------------
def tineye_reverse_image_search(arg: str) -> str:
    """TinEye reverse image search via API.

    Requires:
      • pytineye (`pip install pytineye`)
      • TINEYE_API_KEY in .env

    Arg is URL or local path. Returns JSON summary.
    """
    key = os.getenv("TINEYE_API_KEY")
    if not key:
        return "[tineye_reverse_image_search] set TINEYE_API_KEY in .env"
    try:
        from pytineye import TinEyeAPIRequest
    except ImportError:
        return "[tineye_reverse_image_search] pip install pytineye"
    api = TinEyeAPIRequest(api_key=key)
    if arg.startswith("http"):
        result = api.search_url(arg)
    else:
        result = api.search_data(open(arg, "rb"))
    total = result.get("result", {}).get("total_matches", 0)
    first = result.get("result", {}).get("matches", [{}])[0].get("backlinks", [""])[0]
    return json.dumps({"matches": total, "first": first}, indent=2)


# ---------------------------------------------------------------------------
# Stable Diffusion via OpenAI DALL·E (new 1.0+ interface)
# ---------------------------------------------------------------------------
def stable_diffusion(arg: str) -> str:
    """Generate image via OpenAI DALL·E.

    Requires:
      • OPENAI_API_KEY in .env

    Usage: !tool stable_diffusion "prompt"
    Returns a single image URL.
    """
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        return "[stable_diffusion] set OPENAI_API_KEY in .env"

    try:
        from openai import OpenAI
    except ImportError:
        return "[stable_diffusion] pip install openai"

    client = OpenAI(api_key=key)
    try:
        generation = client.images.generate(
            model="dall-e-3",
            prompt=arg,
            n=1,
            size="1024x1024"
        )
    except Exception as e:
        return f"[stable_diffusion] OpenAI DALL·E error: {e}"

    try:
        return generation.data[0].url
    except Exception:
        return "[stable_diffusion] unexpected response format"


# ---------------------------------------------------------------------------
# Register functions into global TOOLS dict
# ---------------------------------------------------------------------------
import tool_registry

tool_registry.TOOLS.update({
    "google_images_search":         google_images_search,
    "duckduckgo_images":            duckduckgo_images,
    "yandex_reverse_image_search":  yandex_reverse_image_search,
    "tineye_reverse_image_search":  tineye_reverse_image_search,
    "stable_diffusion":             stable_diffusion,
})
