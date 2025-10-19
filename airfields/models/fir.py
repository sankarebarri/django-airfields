from django.db import models
from .airfield import Airfield

class FIR(models.Model):
    """
    Represents a Flight Information Region (FIR) providing ATC and flight information services.
    """
    name = models.CharField(max_length=100, help_text='Full name of the FIR (e.g. Dakar FIR)')
    icao_code = models.CharField(max_length=4, unique=True, help_text='ICAO code (e.g. GOOO)')
    country = models.CharField(max_length=100, help_text='Primary country responsible for this FIR')
    coverage_countries = models.JSONField(blank=True, null=True, help_text='List of countries covered by this FIR')
    fir_type = models.CharField(max_length=10, default='FIR',choices=[
            ('UIR', 'Upper Information Region'),
            ('FIR', 'Flight Information Region'),
        ], help_text='Type of region (e.g. FIR, UIR)')
    upper_limit_ft = models.IntegerField(blank=True, null=True, help_text='Upper altitude limit in feet')
    lower_limit_ft = models.IntegerField(blank=True, null=True, help_text='Lower altitude limit in feet')
    area_km2 = models.FloatField(blank=True, null=True, help_text='Approximate are in km²')
    boundary = models.JSONField(blank=True, null=True, help_text='Boundary coordinates (GeoJSON or list of points)')
    control_centre = models.ForeignKey(Airfield, on_delete=models.SET_NULL, null=True, blank=True,
                                       related_name='controlled_firs', help_text='Main control airfield or ATC centre')
    
    class Meta:
        verbose_name = 'FIR'
        verbose_name_plural = 'FIRs'
        ordering = ['icao_code']

    def __str__(self):
        return f'{self.name} ({self.icao_code})'