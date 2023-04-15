# Generated by Django 4.1.7 on 2023-04-15 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projeto", "0036_remove_pet_nome_abrigo"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("Username", models.CharField(blank=True, max_length=30)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_tutor", models.BooleanField(default=False)),
                ("is_shelter", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
            ],
            options={"abstract": False,},
        ),
    ]