# Generated by Django 4.2.3 on 2023-07-20 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('tipo', models.CharField(choices=[('Serie', 'Serie'), ('Pelicula', 'Pelicula')], max_length=20, null=True)),
                ('no_visualizaciones', models.IntegerField(default=0)),
                ('puntaje', models.DecimalField(decimal_places=1, default=5.0, max_digits=2)),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peliculas.genero')),
            ],
        ),
    ]
