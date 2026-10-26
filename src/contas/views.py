from rest_framework.generics import RetrieveAPIView

from contas.serializers import UsuarioSerializer


class MeView(RetrieveAPIView):
    """Dados e perfil do usuário autenticado, usados pelo front-end após o login."""

    serializer_class = UsuarioSerializer

    def get_object(self):
        return self.request.user
