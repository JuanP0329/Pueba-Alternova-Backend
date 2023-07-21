from random import randint

from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cuentas.models import Acciones, Usuarios, Vista
from .models import Peliculas
from .serializers import PeliculasSerializers


# Create your views here.

class PeliculasList(generics.ListAPIView):
    serializer_class = PeliculasSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Peliculas.objects.all()
        nombre = self.request.query_params.get('nombre', None)
        if nombre is not None:
            queryset = queryset.filter(nombre__icontains=nombre)
        tipo = self.request.query_params.get('tipo', None)
        if tipo is not None:
            queryset = queryset.filter(tipo__icontains=tipo)
        genero = self.request.query_params.get('genero', None)
        if genero is not None:
            queryset = queryset.filter(genero__nombre__icontains=genero)
        return queryset


class PeliculasAleatoriasList(PeliculasList):
    def get_queryset(self):
        queryset = Peliculas.objects.count()
        aleatorio = randint(0, queryset - 1)
        pelicula_aleatoria = Peliculas.objects.all()[aleatorio:aleatorio + 1]
        return pelicula_aleatoria


class PeliculasOrdenadasList(PeliculasList):
    def get_queryset(self):
        queryset = Peliculas.objects.all()
        order_by = self.request.query_params.get('order_by', None)
        if order_by is not None:
            queryset = queryset.order_by(order_by)
            return queryset


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def acciones(request, pk):
    pelicula = Peliculas.objects.filter(pk=pk).first()
    if pelicula:
        id_usuario = request.query_params.get('id_usuario', None)
        usuario = Usuarios.objects.filter(pk=id_usuario).first()
        if usuario:
            calificacion = request.query_params.get('calificacion', None)
            acciones = Acciones(pelicula=pelicula, usuario=usuario, calificacion=calificacion)
            try:
                acciones.save()
                return Response({
                    ' resultado': 'Se califico satisfactoriamente'
                })
            except:
                return Response({
                    ' resultado': 'No puedes volver a calificar esta pelicula'
                })
    return Response({
        'resultado': 'Esta pelicula no existe'
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def accion_vista(request, pk):
    pelicula = Peliculas.objects.filter(pk=pk).first()
    if pelicula:
        id_usuario = request.query_params.get('id_usuario', None)
        usuario = Usuarios.objects.filter(pk=id_usuario).first()
        if usuario:
            vista = Vista(pelicula=pelicula, usuario=usuario, vista=True)
            try:
                vista.save()
                return Response({
                    'resultado': 'Gracias por ver esta pelicula'
                })
            except:
                return Response({
                    'result': 'No puedes volver a ver la pelicula'
                })
    return Response({
        'resultado': 'Esta pelicula no existe'
    })
