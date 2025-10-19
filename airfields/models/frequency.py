from django.db import models
from .airfield import Airfield

class Frequency(models.Model):
    """
    Represents a radio frequency used at an airport (e.g. Tower, Ground, ATIS).
    """
    airfield = models.ForeignKey(Airfield, on_delete=models.CASCADE, related_name='frequencies')
    name = models.CharField(max_length=50, help_text='Frequency name or service (e.g. Tower, ATIC, Ground)')
    frequency_mhz = models.DecimalField(max_digits=6, decimal_places=1, help_text='Frequency in MHZ (e.g. 118.3)')
    remarks = models.CharField(max_length=200, blank=True, null=True,help_text='Additional notes or remarks')

    class Meta:
        verbose_name = 'Frequency'
        verbose_name_plural = 'Frequencies'
        ordering = ['airfield', 'name']

    def __str__(self):
        return f'{self.airfield.icao_code} - {self.name} ({self.frequency_mhz} MHz)'
