from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Planet(models.Model):
    name = models.CharField(max_length=255)
    population = models.BigIntegerField(null=True)
    terrains = ArrayField(models.CharField(max_length=255), blank=True, default=list)
    climates = ArrayField(models.CharField(max_length=255), blank=True, default=list)

    def __str__(self):
        return self.name
