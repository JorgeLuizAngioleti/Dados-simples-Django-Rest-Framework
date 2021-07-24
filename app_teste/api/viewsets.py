from rest_framework.viewsets import ModelViewSet
from app_teste.api.serializers import UsuarioSerializer
from app_teste.models import UsuarioApi
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class UsuarioViewSet(ModelViewSet):
    #permicoes
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    #dados
    queryset = UsuarioApi.objects.all()
    serializer_class = UsuarioSerializer