from django.db import models

class Airfield(models.Model):
    """
    Represents an airfield or airport, including its location, identifiers, and basic data.
    """
    name = models.CharField(max_length=100, help_text='Official airport name')
    icao_code = models.CharField(max_length=4, unique=True, help_text='ICAO code (e.g. GABS for Bamako)')
    iata_code = models.CharField(max_length=3, unique=True, blank=True, null=True,  help_text='IATA code (e.g. BKO for Bamako)')
    city = models.CharField(max_length=100, help_text='City of the airfield')
    country = models.CharField(max_length=100, help_text='Country of the airfield')
    country_code = models.CharField(max_length=2, blank=True, null=True,
                                    help_text="ISO 3166-1 alpha-2 country code, e.g., ML for Mali")
    elevation_ft = models.IntegerField(blank=True, null=True, help_text='Elevation above sea level in feet')
    latitude = models.FloatField(help_text='Latitude in decimal degrees')
    longitude = models.FloatField(help_text='Longitude in decimal degrees')
    timezone = models.CharField(max_length=50, blank=True, null=True, help_text='Timezone identifier (e.g. Africa/Bamako)')
    is_international = models.BooleanField(default=False, help_text='Whether the airport handles international flights')
    date_established = models.DateField(blank=True, null=True, help_text='Date when the airport was establsihed')

    class Meta:
        verbose_name = 'Airfield'
        verbose_name_plural = 'Airfields'
        ordering = ['country', 'city', 'icao_code']

    def __str__(self):
        return f'{self.name} ({self.icao_code})'