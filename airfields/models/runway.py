from django.db import models
from .airfield import Airfield

class Runway(models.Model):
    """
    Represents an airport runway, including its designator, dimensions, and surface type.
    """
    airfield = models.ForeignKey(Airfield, on_delete=models.CASCADE, related_name='runways')
    identifier = models.CharField(max_length=10, help_text='Runway identifier (e.g. 06/24 )')
    length_m = models.IntegerField(help_text='Length in metres')
    width = models.IntegerField(blank=True, null=True, help_text='Width in metres')
    surface_type = models.CharField(max_length=50, help_text='Surface type (e.g. Asphalt, Concrete, Grass)')
    heading = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text='Magnetic heading (°)')
    latitude_threshold = models.FloatField(blank=True, null=True, help_text='Latitude of threshold')
    longitude_threshold = models.FloatField(blank=True, null=True, help_text='Longitude of threshold')

    class Meta:
        verbose_name = 'Runway'
        verbose_name_plural = 'Runways'
        ordering = ['airfield', 'identifier']

    def __str__(self):
        return f'{self.identifier} @ {self.airfield.icao_code}'