from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .managers import UsuariosManager
from peliculas.models import Peliculas

from peliculas.models import Peliculas


# Create your models here.


class Usuarios(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email adress', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UsuariosManager()

    def __str__(self):
        return f'{self.email}'


class Acciones(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE)
    calificacion = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)

    class Meta:
        unique_together = ('usuario', 'pelicula')

    def __str__(self):
        return f'{self.usuario.email} - {self.pelicula.nombre}'

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save(force_insert, force_update, using, update_fields)
        pelicula = Peliculas.objects.get(pk=self.pelicula.pk)
        pelicula.puntaje = (float(pelicula.puntaje) + float(self.calificacion)) / 2
        pelicula.save()


class Vista(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE)
    vista = models.BooleanField(default=False)

    class Meta:
        unique_together = ('usuario', 'pelicula')

    def __str__(self):
        return f'{self.usuario.email} - {self.pelicula.nombre}'

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save(force_insert, force_update, using, update_fields)
        pelicula = Peliculas.objects.get(pk=self.pelicula.pk)
        pelicula.no_visualizaciones = pelicula.no_visualizaciones = pelicula.no_visualizaciones + 1
        pelicula.save()