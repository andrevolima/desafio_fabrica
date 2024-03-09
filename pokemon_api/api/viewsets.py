from rest_framework.response import Response
import requests
from .serializers import PokemonSerializer
from rest_framework.viewsets import ModelViewSet
from ..models import PokemonModel
import json





class PokemonViewSet(ModelViewSet):
    queryset = PokemonModel.objects.all()
    serializer_class = PokemonSerializer

    def create(self, request):
        name = request.data.get('name')

        site = f'https://pokeapi.co/api/v2/pokemon/{name}/'

        requisicao = requests.get(site)

        if requisicao.status_code == 200:
                    pokemon_data = requisicao.json()
                    serializer = self.get_serializer(data=pokemon_data)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    return Response(serializer.data)
        else:
            return Response({'ERRO': 'Nao foi possivel pegar os dados dos pokemanos'}, status=requisicao.status_code)

      