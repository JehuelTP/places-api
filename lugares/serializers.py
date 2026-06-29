from rest_framework import serializers
from .models import Lugar, Horario, Foto, ComentarioLugar, Favorito


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'


class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = '__all__'


class ComentarioLugarSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.id')

    class Meta:
        model = ComentarioLugar
        fields = '__all__'


class FavoritoSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.id')

    class Meta:
        model = Favorito
        fields = '__all__'


class LugarSerializer(serializers.ModelSerializer):
    horarios = HorarioSerializer(many=True, read_only=True)
    fotos = FotoSerializer(many=True, read_only=True)
    comentarios = ComentarioLugarSerializer(many=True, read_only=True)

    class Meta:
        model = Lugar
        fields = '__all__'