import requests
from django.conf import settings


def get_reverse_geocoded_address(latitude, longitude):
    """Return the reverse geocoded address from the coordinate"""
    url = f"{settings.RADAR_BASE_URL}/v1/geocode/reverse?coordinates={latitude},{longitude}"
    headers = {"Authorization": settings.RADAR_API_KEY}
    resp = requests.get(url, headers=headers, timeout=60)

    if resp.ok:
        addresses = resp.json().get("addresses", [])

        if addresses:
            return addresses[0]["formattedAddress"]

    return None
