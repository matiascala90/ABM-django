# Generated by Django 5.1 on 2024-09-04 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0003_alter_compania_nombre_compania'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compania',
            name='nombre_compania',
            field=models.CharField(max_length=255),
        ),
    ]
