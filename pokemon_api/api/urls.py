from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .viewsets import PokemonViewSet

router = DefaultRouter()

router.register(prefix="pokemon", viewset=PokemonViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
