Para iniciar a aplicacao:
Pra fazer o projeto rodar, vai ser necessario clonar o repositório do git e criar um ambiente virtual. Em seguida, instale essas dependências com o comando pip install.

Dependências Necessárias (Instaladas com pip install):

django: para instalar o django, um framework web parao Python.
djangorestframework: Para instalar o djangorest.
requests: Biblioteca para fazer requisições
psycopg2: PostgreSQL para Python.
djangorestframework-simplejwt: Implementação JWT para autenticação em APIs Django REST.

Banco de Dados:
O PostgreSQL foi utilizado como banco de dados para armazenar informações sobre os Pokémon apos a requisicao ser feita. A configuração dele foi ajustada no arquivo settings.py para se rodar na configuração local da maquina.

Inicialização e Acesso à API:
Inicie o servidor da aplicação com o comando python manage.py runserver e acesse a API no navegador em http://127.0.0.1:8000/api/ para explorar os recursos disponíveis. Caso queira ver os pokemons ja cadastrados http://127.0.0.1:8000/api/pokemon/  

Utilização no Insomnia:
Para interagir com a API, use o Insomnia. Vai ser necessario se autenticar obtendo um token JWT através de uma requisição POST para http://localhost:8000/api/token/ com as o username e a password do superusuário criado. Lembre de colocar o token nas Headers, coloque "Authorization" na header e Bearer "toke" no value  Com o token, você pode realizar operações get, post, put e delete nos Pokémon, pode listar todos, obter detalhes de um específico, adicionar, atualizar ou excluir eles. Para adicionar um novo pokemon bastaa digitar "name": "nome do pokemon" e dar um get. 

