from django.db import models


class Inscricao(models.Model):
    """Inscrição do aluno em uma edição, com a turma que recebe o bônus (UC02)."""

    class Status(models.TextChoices):
        CONFIRMADA = 'CONFIRMADA', 'Confirmada'
        CANCELADA = 'CANCELADA', 'Cancelada'

    aluno = models.ForeignKey('academico.Aluno', on_delete=models.PROTECT, related_name='inscricoes')
    edicao = models.ForeignKey('edicoes.Edicao', on_delete=models.PROTECT, related_name='inscricoes')
    turma = models.ForeignKey(
        'academico.Turma',
        on_delete=models.PROTECT,
        related_name='inscricoes',
        help_text='Turma que recebe o bônus.',
    )
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.CONFIRMADA)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'inscrição'
        verbose_name_plural = 'inscrições'
        constraints = [
            # RN01: uma inscrição por aluno em cada edição.
            models.UniqueConstraint(fields=['aluno', 'edicao'], name='uniq_inscricao_aluno_edicao'),
        ]

    def __str__(self):
        return f'{self.aluno} - {self.edicao}'
