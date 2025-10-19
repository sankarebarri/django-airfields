from django.db import models
from .fir import FIR
from .waypoint import Waypoint

class Airway(models.Model):
    """
    Represents an airway route connecting a series of waypoints.
    """
    name = models.CharField(max_length=10, unique=True, help_text='Airway name (e.g. UA612)')
    fir = models.ForeignKey(FIR, on_delete=models.SET_NULL, null=True, blank=True, related_name='airways')
    direction = models.CharField(max_length=10, default='BI', choices=[
        ('BI', 'BI'),
        ('UNI', 'UNI'),
    ], help_text='Direction: BI (Biderectional) or UNI(Uniderectional)')
    upper_limit_ft = models.IntegerField(blank=True, null=True, help_text='Upper altitude limit in feet')
    lower_limit_ft = models.IntegerField(blank=True, null=True, help_text='Lower altitude limit in feet')
    remarks = models.TextField(blank=True, null=True)
    waypoints = models.ManyToManyField(Waypoint, related_name='airways', blank=True)

    class Meta:
        verbose_name = 'Airway'
        verbose_name_plural = 'Airways'
        ordering = ['name']

    def __str__(self):
        return self.name
    

# Later when we'll need distances between points, altitudes, restrictions, etc
# class AirwaySegment(models.Model):
#     """
#     Intermediate model defining the ordered sequence of waypoints in an airway.
#     """
#     pass