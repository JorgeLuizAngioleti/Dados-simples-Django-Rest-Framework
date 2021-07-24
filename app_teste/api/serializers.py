
from rest_framework.serializers import ModelSerializer
from app_teste.models import UsuarioApi,  Escola
from django.contrib.auth.models import User

class EscolaSerializer(ModelSerializer):
    class Meta:
        model = Escola
        fields = ('nome',)

class UsuarioSerializer(ModelSerializer):
    # mostrar relacionamentos
    escola = EscolaSerializer(many=True)
    class Meta:
        model = UsuarioApi
        fields =('id','nome','usuario','escola','idade')
