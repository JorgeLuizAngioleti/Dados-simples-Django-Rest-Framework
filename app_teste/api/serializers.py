from rest_framework.serializers import ModelSerializer
from app_teste.models import UsuarioApi

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = UsuarioApi
        fields =('id','nome','usuario','idade')