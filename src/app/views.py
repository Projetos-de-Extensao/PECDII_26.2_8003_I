from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from app.models import Produto
from app.serializers import ProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    # Exemplo didático do guia EchoAPI: aberto, sem login.
    permission_classes = [AllowAny]
