from django.contrib import admin

from .models import Usuarios, Acciones, Vista


# Register your models here.
@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_staff', 'is_active', ]
    list_display_links = list_display


@admin.register(Acciones)
class AccionesAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'pelicula', 'calificacion']
    list_display_links = list_display


@admin.register(Vista)
class VistaAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'pelicula', 'vista']
    list_display_links = list_display
