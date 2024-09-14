from django.db import models

class Telescope(models.Model):
    name = models.CharField(max_length=255, unique=True)
    manufacturer = models.CharField(max_length=255)  # Changed name for clarity
    aperture = models.DecimalField(max_digits=10, decimal_places=2)  # May need decimals
    focal_length = models.IntegerField()  # Changed name for consistency
    focal_ratio = models.DecimalField(max_digits=5, decimal_places=2)  # May need decimals

    def __str__(self):
        return self.name
