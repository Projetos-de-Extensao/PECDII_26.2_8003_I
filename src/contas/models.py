from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    """Usuário institucional (UC01). O perfil define o painel e as permissões (RF-02)."""

    class Perfil(models.TextChoices):
        ALUNO = 'aluno', 'Aluno'
        PROFESSOR = 'professor', 'Professor'
        COORDENACAO = 'coordenacao', 'Coordenação de curso'
        ADMINISTRACAO = 'administracao', 'Administração acadêmica'

    perfil = models.CharField(max_length=20, choices=Perfil.choices, default=Perfil.ALUNO)
    matricula = models.CharField(
        'matrícula/SIAPE', max_length=20, unique=True, null=True, blank=True,
        help_text='Matrícula do aluno ou SIAPE do servidor.',
    )

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

    def __str__(self):
        return self.get_full_name() or self.username
