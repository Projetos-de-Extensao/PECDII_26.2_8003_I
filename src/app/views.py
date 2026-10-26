# app/api.py
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from app.models import Produto
from app.serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    # Exemplo didático do guia EchoAPI: aberto, sem login.
    permission_classes = [AllowAny]
