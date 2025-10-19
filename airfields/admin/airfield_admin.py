from django.contrib import admin
from airfields.models import Airfield, Runway, Frequency

@admin.register(Airfield)
class AirfieldAdmin(admin.ModelAdmin):
    list_display = ("name", "icao_code", "iata_code", "city", "country", "is_international")
    search_fields = ("name", "icao_code", "iata_code", "city", "country")



@admin.register(Runway)
class RunwayAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'airfield', 'length_m', 'surface_type')
    list_filter = ('surface_type',)
    search_fields = ('identifier', 'airfield__name', 'airfield__icao_code')


@admin.register(Frequency)
class FrequencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'airfield', 'frequency_mhz')
    search_fields = ('name', 'airfield__name', 'airfield__icao_code')