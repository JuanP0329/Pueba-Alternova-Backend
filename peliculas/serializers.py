from rest_framework import serializers
from .models import Peliculas, Genero
from cuentas.models import Acciones


class PeliculasSerializers(serializers.ModelSerializer):
    genero = 'GeneroSerializers'

    class Meta:
        model = Peliculas
        fields = '__all__'


class GeneroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'


class AccionesSerializers(serializers.ModelSerializer):
    pelicula = PeliculasSerializers

    class Meta:
        model = Acciones
        fields = '__all__'
