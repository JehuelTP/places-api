from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Lugar, Horario, Foto, ComentarioLugar, Favorito
from .serializers import (
    LugarSerializer,
    HorarioSerializer,
    FotoSerializer,
    ComentarioLugarSerializer,
    FavoritoSerializer,
)


class LugarViewSet(viewsets.ModelViewSet):
    queryset = Lugar.objects.all().order_by('-creado')
    serializer_class = LugarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        'nombre',
        'descripcion',
        'provincia',
        'municipio',
        'departamento',
        'ubicacion',
    ]

    ordering_fields = [
        'nombre',
        'provincia',
        'municipio',
        'departamento',
        'creado',
        'actualizado',
    ]

    ordering = ['-creado']

    def get_queryset(self):
        queryset = Lugar.objects.all()

        departamento = self.request.query_params.get('departamento')
        provincia = self.request.query_params.get('provincia')
        municipio = self.request.query_params.get('municipio')

        if departamento:
            queryset = queryset.filter(departamento__icontains=departamento)

        if provincia:
            queryset = queryset.filter(provincia__icontains=provincia)

        if municipio:
            queryset = queryset.filter(municipio__icontains=municipio)

        return queryset


class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FotoViewSet(viewsets.ModelViewSet):
    queryset = Foto.objects.all().order_by('-fecha_subida')
    serializer_class = FotoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ComentarioLugarViewSet(viewsets.ModelViewSet):
    queryset = ComentarioLugar.objects.all().order_by('-fecha')
    serializer_class = ComentarioLugarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all().order_by('-fecha')
    serializer_class = FavoritoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorito.objects.filter(usuario=self.request.user).order_by('-fecha')

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)