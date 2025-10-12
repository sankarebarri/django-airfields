from django.contrib import admin
from airfields.models import Airfield

@admin.register(Airfield)
class AirfieldAdmin(admin.ModelAdmin):
    list_display = ("name", "icao_code", "iata_code", "city", "country", "is_international")
    search_fields = ("name", "icao_code", "iata_code", "city", "country")
