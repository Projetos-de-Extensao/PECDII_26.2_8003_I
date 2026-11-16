from django.core.exceptions import ValidationError
from django.db import models


class Campus(models.Model):
    """Campus onde a prova pode ser aplicada (UC07)."""

    nome = models.CharField(max_length=80, unique=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'campus'
        verbose_name_plural = 'campi'

    def __str__(self):
        return self.nome


class Edicao(models.Model):
    """Uma aplicação do Teste de Progresso em um semestre (UC05, RF-05 a RF-07)."""

    class Status(models.TextChoices):
        PLANEJADA = 'PLANEJADA', 'Planejada'
        INSCRICOES_ABERTAS = 'INSCRICOES_ABERTAS', 'Inscrições abertas'
        ENCERRADA = 'ENCERRADA', 'Encerrada'

    semestre = models.CharField(max_length=6, unique=True, help_text='Ex.: 2026.2')
    data_prova = models.DateField('data da prova')
    inicio_inscricao = models.DateTimeField('início da inscrição')
    fim_inscricao = models.DateTimeField('fim da inscrição')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PLANEJADA)
    campi = models.ManyToManyField(Campus, related_name='edicoes', blank=True)
    cursos = models.ManyToManyField('academico.Curso', related_name='edicoes', blank=True)

    class Meta:
        ordering = ['-semestre']
        verbose_name = 'edição'
        verbose_name_plural = 'edições'

    def clean(self):
        if self.inicio_inscricao and self.fim_inscricao and self.fim_inscricao <= self.inicio_inscricao:
            raise ValidationError({'fim_inscricao': 'O fim da inscrição deve ser depois do início.'})

    def __str__(self):
        return f'Teste de Progresso {self.semestre}'
