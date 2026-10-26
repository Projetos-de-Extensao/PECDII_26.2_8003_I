from rest_framework.permissions import BasePermission

from contas.models import Usuario


class PerfilPermission(BasePermission):
    """Libera o acesso apenas aos perfis listados em `perfis`."""

    perfis = ()

    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and user.perfil in self.perfis)


class IsAluno(PerfilPermission):
    perfis = (Usuario.Perfil.ALUNO,)


class IsProfessor(PerfilPermission):
    perfis = (Usuario.Perfil.PROFESSOR,)


class IsCoordenacao(PerfilPermission):
    perfis = (Usuario.Perfil.COORDENACAO,)


class IsAdministracao(PerfilPermission):
    perfis = (Usuario.Perfil.ADMINISTRACAO,)
