# Generated by Django 4.1.7 on 2023-04-01 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projeto", "0006_alter_tutor_cidade"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tutor", name="nome", field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="tutor", name="telefone", field=models.CharField(max_length=25),
        ),
    ]