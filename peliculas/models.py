from django.db import models
from django import forms

# Create your models here.


class Peliculas(models.Model):
    OPCIONES = [('Serie', 'Serie'), ('Pelicula', 'Pelicula')]

    id = models.CharField(primary_key=True, max_length=100)
    nombre = models.CharField(max_length=200)
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=OPCIONES, null=True)
    no_visualizaciones = models.IntegerField(default=0)
    puntaje = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)

    def __str__(self):
        return f'{self.nombre}'


class PelisculaForm(forms.ModelForm):
    class Meta:
        model = Peliculas
        fields = ['tipo']
        widgets = {
            'condicion': forms.RadioSelect
        }


class Genero(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nombre}'

