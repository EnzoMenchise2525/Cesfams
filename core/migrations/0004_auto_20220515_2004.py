# Generated by Django 3.2.3 on 2022-05-16 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_medicamento_resetap'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resetap',
            old_name='fecha_consumo',
            new_name='fecha_Consumo',
        ),
        migrations.RenameField(
            model_name='resetap',
            old_name='medic',
            new_name='medicamento',
        ),
        migrations.RenameField(
            model_name='resetap',
            old_name='nombreCompleto',
            new_name='nombre_Completo',
        ),
    ]
