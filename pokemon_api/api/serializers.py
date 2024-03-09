from rest_framework import serializers
from ..models import PokemonModel

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonModel
        fields = ["id","name", "height", "weight"] 
