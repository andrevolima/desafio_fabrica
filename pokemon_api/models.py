from django.db import models

class PokemonModel(models.Model):
    # Definindo os campos armazenar o dados do pokemon
    name = models.CharField(max_length=100, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    def __str__(self):
        # retronando o nome do pokemn quando converto para string
        return self.name
