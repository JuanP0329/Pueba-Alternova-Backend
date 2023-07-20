from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('v1/peliculas', PeliculasList.as_view()),
    path('v1/peliculas/aleatorias', PeliculasAleatoriasList.as_view()),
    path('v1/peliculas/ordenadas', PeliculasOrdenadasList.as_view()),
    path('v1/peliculas/<str:pk>/calificar', acciones),
    path('v1/peliculas/<str:pk>/ver', accion_vista)

]

