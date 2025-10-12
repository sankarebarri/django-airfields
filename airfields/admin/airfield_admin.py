from django.contrib import admin
from airfields.models import Airfield

@admin.register(Airfield)
class AirfieldAdmin(admin.ModelAdmin):
    list_display = ("icao_code", "name", "city", "country")
    search_fields = ("icao_code", "iata_code", "name")
