# Generated by Django 4.2.3 on 2023-07-19 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0006_genero_alter_peliculas_genero'),
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='modelos',
        ),
        migrations.AddField(
            model_name='usuarios',
            name='peliculas',
            field=models.ManyToManyField(blank=True, null=True, to='peliculas.peliculas'),
        ),
    ]