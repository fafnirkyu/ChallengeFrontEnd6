# Generated by Django 4.1.7 on 2023-04-03 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projeto", "0008_pet_adotado_pet_foto_pet_pet_idade_pet_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="abrigo", name="pet",),
    ]