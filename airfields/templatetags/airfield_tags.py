from django import template
from airfields.models import Airfield

register = template.Library()


@register.simple_tag
def airfield_name(code):
    """
    Usage: {% airfield_name "GABS" %}
    Output: Bamako Senou International Airport (GABS)
    """
    if not code:
        return ""

    code = code.strip().upper()
    airfield = (
        Airfield.objects.filter(icao_code=code).first()
        or Airfield.objects.filter(iata_code=code).first()
    )

    if airfield:
        return f"{airfield.name} ({code})"
    return f"{code} (unknown)"


@register.simple_tag
def airport_flag(code):
    """
    Usage: {% airport_flag "BKO" %}
    Output: 🇲🇱 (or 🏳️ if unknown)
    """
    if not code:
        return ""

    code = code.strip().upper()
    airfield = (
        Airfield.objects.filter(icao_code=code).first()
        or Airfield.objects.filter(iata_code=code).first()
    )

    if not airfield or not getattr(airfield, "country_code", None):
        return "🏳️"  # fallback flag

    return _country_code_to_flag(airfield.country_code)


def _country_code_to_flag(country_code):
    """
    Convert ISO country code (e.g., 'ML') to emoji flag (🇲🇱).
    """
    try:
        return "".join(chr(ord(char) + 127397) for char in country_code.upper())
    except Exception:
        return "🏳️"
