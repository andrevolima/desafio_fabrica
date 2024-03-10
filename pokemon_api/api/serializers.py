from rest_framework import serializers
from ..models import PokemonModel

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        # define o model e os campos a serem usados no serializador
        model = PokemonModel
        # Define os campos a serem incluidos no serializador
        fields = ["id","name", "height", "weight"] 
