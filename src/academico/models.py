from django.conf import settings
from django.db import models


class Curso(models.Model):
    codigo = models.CharField('código', max_length=20, unique=True)
    nome = models.CharField(max_length=120)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    codigo = models.CharField('código', max_length=20, unique=True)
    nome = models.CharField(max_length=120)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f'{self.codigo} - {self.nome}'


class Turma(models.Model):
    """Turma de uma disciplina. É a turma escolhida pelo aluno para receber o bônus."""

    codigo = models.CharField('código', max_length=20)
    semestre = models.CharField(max_length=6, help_text='Ex.: 2026.2')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT, related_name='turmas')
    professor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='turmas',
        limit_choices_to={'perfil': 'professor'},
    )

    class Meta:
        ordering = ['semestre', 'codigo']
        constraints = [
            models.UniqueConstraint(fields=['codigo', 'semestre'], name='uniq_turma_codigo_semestre'),
        ]

    def __str__(self):
        return f'{self.codigo} ({self.semestre}) - {self.disciplina.nome}'


class Aluno(models.Model):
    """Dados acadêmicos do aluno. Nome, matrícula e e-mail ficam no Usuario (1–1)."""

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='aluno',
        limit_choices_to={'perfil': 'aluno'},
    )
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name='alunos')
    campus = models.ForeignKey('edicoes.Campus', on_delete=models.PROTECT, related_name='alunos')
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['usuario__first_name', 'usuario__last_name']

    @property
    def matricula(self):
        return self.usuario.matricula

    @property
    def nome(self):
        return self.usuario.get_full_name() or self.usuario.username

    @property
    def email(self):
        return self.usuario.email

    def __str__(self):
        return f'{self.matricula} - {self.nome}'
