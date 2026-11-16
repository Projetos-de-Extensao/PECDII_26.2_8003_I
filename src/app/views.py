from django.db.models import ProtectedError
from rest_framework import status, viewsets
from rest_framework.response import Response

from app.models import Aluno, Inscricao
from app.serializers import AlunoSerializer, InscricaoSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    def destroy(self, request, *args, **kwargs):
        # O model usa on_delete=PROTECT: aluno com inscricao nao pode ser apagado
        try:
            return super().destroy(request, *args, **kwargs)
        except ProtectedError:
            return Response(
                {'detail': 'Aluno possui inscrições e não pode ser excluído. Desative-o (ativo = false).'},
                status=status.HTTP_409_CONFLICT,
            )


class InscricaoViewSet(viewsets.ModelViewSet):
    # select_related traz o aluno na mesma consulta SQL
    queryset = Inscricao.objects.select_related('aluno').all()
    serializer_class = InscricaoSerializer