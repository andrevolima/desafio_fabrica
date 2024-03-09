from django.db import models

class PokemonModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
