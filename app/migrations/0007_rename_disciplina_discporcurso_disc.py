# Generated by Django 5.0.3 on 2024-04-01 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_tipoaval_tipoavaliacao_tipovaliacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discporcurso',
            old_name='disciplina',
            new_name='disc',
        ),
    ]
