from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

letrasregex = RegexValidator(r'^[a-zA-Z_ áàâãéèêíïóôõöúçñ]*$', 'Não inclua números neste campo')

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    Username = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_tutor = models.BooleanField("É Tutor", default=False)
    is_shelter = models.BooleanField("É Abrigo", default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Tutor(models.Model):
    id_tutor = models.AutoField(primary_key=True)
    email_tutor = models.EmailField("Email" ,max_length=255, unique=True)
    nome = models.CharField("Nome completo", max_length=255,validators=[letrasregex])
    telefone = models.CharField("Telefone", max_length=25)
    cidade = models.CharField(max_length=255,validators=[letrasregex])
    sobre = models.CharField(max_length=255, validators=[letrasregex])
    foto_tutor = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Abrigo(models.Model):
    id_abrigo = models.AutoField(primary_key=True)
    email_abrigo = models.EmailField(max_length=255, unique=True)
    nome_abrigo = models.CharField(max_length=255, validators=[letrasregex])
    telefone_abrigo = models.CharField(max_length=25)
    cidade_abrigo = models.CharField(max_length=255,validators=[letrasregex])
    sobre_abrigo = models.CharField(max_length=255)
    foto_abrigo = models.ImageField(blank=True, null=True)

class Pet(models.Model):
    id_pet = models.AutoField(primary_key=True)
    nome_pet = models.CharField(max_length=30,validators=[letrasregex])
    cidade_pet = models.CharField(max_length=50,validators=[letrasregex])
    idade_pet = models.CharField(max_length=255, blank=True, null=True)
    sobre_pet = models.CharField(max_length=255,validators=[letrasregex])
    adotado = models.BooleanField(default=False)
    foto_pet = models.ImageField(blank=True, null=True)
    def __str__(self):
        return self.nome_pet    


class Adocao(models.Model):
    id_adocao = models.AutoField(primary_key=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    data_adocao = models.DateField()