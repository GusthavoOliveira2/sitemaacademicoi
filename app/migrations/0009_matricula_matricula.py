# Generated by Django 5.0.3 on 2024-04-01 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_discporcurso_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='matricula',
            field=models.CharField(default='0000', max_length=100, verbose_name='Matricula'),
            preserve_default=False,
        ),
    ]