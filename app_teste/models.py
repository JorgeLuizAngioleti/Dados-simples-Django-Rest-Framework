from django.db import models
from django.contrib.auth.models import User

class UsuarioApi(models.Model):
    nome = models.CharField(max_length=150)
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
