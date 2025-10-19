from django.contrib import admin
from airfields.models import (Airfield, Runway, Frequency, FIR, Waypoint, Airway)

@admin.register(Airfield)
class AirfieldAdmin(admin.ModelAdmin):
    list_display = ("name", "icao_code", "iata_code", "city", "country", "is_international")
    search_fields = ("name", "icao_code", "iata_code", "city", "country")

@admin.register(Runway)
class RunwayAdmin(admin.ModelAdmin):
    list_display = ("identifier", "airfield", "length_m", "surface_type", "heading")
    list_filter = ("surface_type", "airfield")
    search_fields = ("identifier", "airfield__icao_code", "airfield__name")

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("airfield")

@admin.register(Frequency)
class FrequencyAdmin(admin.ModelAdmin):
    list_display = ("airfield", "name", "frequency_mhz", "remarks")
    list_filter = ("airfield",)
    search_fields = ("airfield__icao_code", "airfield__name", "name")


@admin.register(FIR)
class FIRAdmin(admin.ModelAdmin):
    list_display = ('name', 'icao_code', 'country', 'fir_type', 'control_centre')
    search_fields = ('name', 'icao_code', 'country')
    list_filter = ('fir_type', 'country')

@admin.register(Waypoint)
class WaypointAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'waypoint_type', 'fir', 'latitude', 'longitude')
    search_fields = ('identifier', 'fir__name', 'fir__icao_code')
    list_filter = ('waypoint_type',)

@admin.register(Airway)
class AirwayAdmin(admin.ModelAdmin):
    list_display = ('name', 'fir', 'direction', 'lower_limit_ft', 'upper_limit_ft')
    search_fields = ('name', 'fir__name', 'fir__icao_code')
    list_filter = ('direction',)