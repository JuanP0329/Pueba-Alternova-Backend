# Generated by Django 4.2.3 on 2023-07-18 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0003_alter_peliculas_no_visualizaciones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peliculas',
            name='puntaje',
        ),
    ]
