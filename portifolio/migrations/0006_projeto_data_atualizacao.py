# Generated by Django 5.0.4 on 2024-04-23 19:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0005_projeto_data_postagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='data_atualizacao',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
