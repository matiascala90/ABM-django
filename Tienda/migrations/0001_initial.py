# Generated by Django 5.1 on 2024-09-02 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_compania', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_genero', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Plataforma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_plataforma', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('foto', models.ImageField(upload_to='')),
                ('precio', models.FloatField()),
                ('compania', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.compania')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.genero')),
                ('plataforma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.plataforma')),
            ],
        ),
    ]
