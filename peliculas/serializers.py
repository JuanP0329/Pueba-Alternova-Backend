from rest_framework import serializers

from cuentas.models import Acciones
from .models import Peliculas, Genero


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
