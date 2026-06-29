from django.contrib import admin
from django.contrib.admin.sites import NotRegistered

from .models import Lugar, Horario, Foto, ComentarioLugar, Favorito


for model in [Lugar, Horario, Foto, ComentarioLugar, Favorito]:
    try:
        admin.site.unregister(model)
    except NotRegistered:
        pass


@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'provincia', 'municipio', 'departamento')
    search_fields = ('nombre', 'provincia', 'municipio', 'departamento')
    list_filter = ('provincia', 'departamento')


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'lugar', 'dia', 'hora_inicio', 'hora_fin')
    list_filter = ('dia',)


@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'lugar', 'descripcion', 'fecha_subida')
    search_fields = ('descripcion', 'lugar__nombre')


@admin.register(ComentarioLugar)
class ComentarioLugarAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'lugar', 'calificacion', 'fecha')
    list_filter = ('calificacion', 'fecha')


@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'lugar', 'fecha')