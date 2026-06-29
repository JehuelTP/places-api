from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    LugarViewSet,
    HorarioViewSet,
    FotoViewSet,
    ComentarioLugarViewSet,
    FavoritoViewSet,
)

router = DefaultRouter()

router.register(r'lugares', LugarViewSet, basename='lugares')
router.register(r'horarios', HorarioViewSet, basename='horarios')
router.register(r'fotos', FotoViewSet, basename='fotos')
router.register(r'comentarios', ComentarioLugarViewSet, basename='comentarios')
router.register(r'favoritos', FavoritoViewSet, basename='favoritos')

urlpatterns = [
    path('', include(router.urls)),
]