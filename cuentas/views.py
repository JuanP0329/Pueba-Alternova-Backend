from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Acciones
from peliculas.serializers import AccionesSerializers
from peliculas.models import Peliculas


@api_view(['POST'])
def calificar_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Peliculas, id=pelicula_id)
    usuario = request.user
    calificacion = request.data.get('calificacion')

    accion, created = Acciones.objects.get_or_create(usuario=usuario, pelicula=pelicula)
    accion.calificacion = calificacion
    accion.save()

    serializer = AccionesSerializers(accion)
    return Response(serializer.data)
