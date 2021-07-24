
from rest_framework.serializers import ModelSerializer
from app_teste.models import UsuarioApi
from django.contrib.auth.models import User
'''
# mostrar relacionamentos
atracoes = AtracaoSerializer(many=True)
enderecos = EnderecosSerializer()
'''
class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = UsuarioApi
        fields =('id','nome','usuario','idade')
