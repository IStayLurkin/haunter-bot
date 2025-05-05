"""Geopy geocode / reverse‑geocode

If arg looks like 'lat,lon' → reverse‑geocode.
Else → forward‑geocode the place string.
"""
import re
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="kiba_bot")
LATLON = re.compile(r"^\\s*(-?\\d+(?:\\.\\d+)?),\\s*(-?\\d+(?:\\.\\d+)?)\\s*$")

def geopy(arg: str):
    """
    Geocode an address or coordinates using OpenStreetMap (Nominatim).

    **Usage**

    `!tool geopy "<address or lat,long>"`

    *Examples*
    ```
    !tool geopy "10 Downing St, London"
    !tool geopy "48.8583,2.2944"
    ```

    Returns: `geopy.location.Location` string with full address and (lat, lon)
    """
    g = Nominatim(user_agent="kiba-bot")
    loc = g.geocode(arg)
    return str(loc) if loc else "No match found."