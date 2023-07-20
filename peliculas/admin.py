from django.contrib import admin
from .models import Peliculas, Genero


# Register your models here.


@admin.register(Peliculas)
class PeliculasAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'genero', 'tipo', 'no_visualizaciones', 'puntaje']
    list_display_links = list_display
    readonly_fields = ['no_visualizaciones', 'puntaje']


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    list_display_links = list_display
