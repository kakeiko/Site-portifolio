# Generated by Django 5.0.4 on 2024-04-23 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0009_projeto_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='texto_objetivo',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projeto',
            name='texto_projeto',
            field=models.CharField(default=2, max_length=1000),
            preserve_default=False,
        ),
    ]
