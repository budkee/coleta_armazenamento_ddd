# Generated by Django 5.0.6 on 2024-06-09 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coleta_armazena_mysql', '0002_alter_previsao_data_hora'),
    ]

    operations = [
        migrations.RenameField(
            model_name='previsao',
            old_name='data_hora',
            new_name='data_hora_previsao',
        ),
    ]