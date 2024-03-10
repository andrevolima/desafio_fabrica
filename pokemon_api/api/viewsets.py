from rest_framework.response import Response
import requests
from .serializers import PokemonSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..models import PokemonModel
import json





class PokemonViewSet(ModelViewSet):
    # Define a permissão para acesso
    permission_classes = (IsAuthenticated, )

    # Define o conjunto de dados como todos os objetos PokemonModel no banco de dados
    queryset = PokemonModel.objects.all()

    # Define o serializador para converter dados em JSON
    serializer_class = PokemonSerializer

    def create(self, request):
        # Obtem o nome do pokemon a partir dos dados da requisicao
        name = request.data.get('name')

        # Constroi a URL da API de pokemon com base no nome fornecido
        site = f'https://pokeapi.co/api/v2/pokemon/{name}/'

        #Faz uma requisicao a api
        requisicao = requests.get(site)

        # Verifica se a requisição foi bem-sucedida
        if requisicao.status_code == 200:
                    #c Converte os dados do pokemon pra json
                    pokemon_data = requisicao.json()
                    # instancia o serializer, passando os dados do poekmon
                    serializer = self.get_serializer(data=pokemon_data)

                    # Verifica se os dados sao validos
                    serializer.is_valid(raise_exception=True)

                    # salva os dados do pokemon no banco
                    serializer.save()

                    # retorna os dados do pokemon
                    return Response(serializer.data)
        else:
            # Retorna uma resposta de erro
            return Response({'ERRO': 'Nao foi possivel pegar os dados dos pokemanos'}, status=requisicao.status_code)

      