# Generated by Django 4.1.7 on 2023-04-13 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projeto", "0035_rename_abrigo_pet_nome_abrigo"),
    ]

    operations = [
        migrations.RemoveField(model_name="pet", name="nome_abrigo",),
    ]
