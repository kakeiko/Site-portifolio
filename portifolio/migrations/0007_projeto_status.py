# Generated by Django 5.0.4 on 2024-04-23 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0006_projeto_data_atualizacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='status',
            field=models.CharField(choices=[('Finalizado', 'Finalizado'), ('Em andamento', 'Em andamento')], default='', max_length=100),
        ),
    ]
