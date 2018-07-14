from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class kenya(models.Model):
    unit_area = models.FloatField()
    unit_perim = models.FloatField()
    district = models.CharField(max_length=50)
    count = models.FloatField()
    county_nam = models.CharField(max_length=50)
    code = models.BigIntegerField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.county_nam

class checkpoint(models.Model):
    name = models.CharField(max_length=50)
    location = models.PointField(srid=4326)

    def __str__(self):
        return self.name

class Lan(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.CharField(max_length=50)

    def __str__(self):
        return self.name

