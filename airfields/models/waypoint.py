from django.db import models
from .fir import FIR

class Waypoint(models.Model):
    """
    Represents a navigation waypoint or fix used for routing.
    """
    identifier = models.CharField(max_length=10, unique=True, help_text='Waypoint name or identifier (e.g. ETRUL)')
    latitude = models.FloatField(help_text='Latitude in decimal degrees')
    longitude = models.FloatField(help_text='Longitude in decimal degrees')
    waypoint_type = models.CharField(max_length=20, default='ENROUTE', choices=[
        ('ENROUTE', 'Enroute'),
        ('TERMINAL', 'Terminal'),
        ('APPROACH', 'Approach'),
    ])
    marker = models.CharField(max_length=20, choices=[
        ('NDB', 'NDB'),
        ('FIX', 'FIX'),
        ('VOR', 'VOR'),
    ])
    fir = models.ForeignKey(FIR, on_delete=models.SET_NULL, null=True, blank=True, related_name='waypoints')
    description = models.TextField(blank=True, null=True, help_text='Optional description or notes')

    class Meta:
        verbose_name = 'Waypoint'
        verbose_name_plural = 'Waypoints'
        ordering = ['identifier']

    def __str__(self):
        return self.identifier