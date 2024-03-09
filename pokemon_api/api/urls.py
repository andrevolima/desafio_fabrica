from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .viewsets import PokemonViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()

router.register(prefix="pokemon", viewset=PokemonViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())
]
