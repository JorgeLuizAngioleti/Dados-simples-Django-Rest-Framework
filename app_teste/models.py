from django.db import models
from django.contrib.auth.models import User


class Escola(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class UsuarioApi(models.Model):
    nome = models.CharField(max_length=150)
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    escola = models.ManyToManyField(Escola)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
