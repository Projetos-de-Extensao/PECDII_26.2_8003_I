from django.db import models
from django.db.models import Q

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
        
class Aluno(models.Model):
    matricula = models.CharField(max_length=12, unique=True)
    nome = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    curso = models.CharField(max_length=80)
    campus = models.CharField(max_length=40)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.matricula} - {self.nome}"


class Inscricao(models.Model):
    class Status(models.TextChoices):
        ATIVA = "ATIVA", "Ativa"
        CANCELADA = "CANCELADA", "Cancelada"

    aluno = models.ForeignKey(
        Aluno, on_delete=models.PROTECT, related_name="inscricoes"
    )
    edicao = models.CharField(max_length=10)
    turma_codigo = models.CharField(max_length=20)
    disciplina = models.CharField(max_length=80)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.ATIVA
    )
    atendimento_especial = models.BooleanField(default=False)
    numero_comprovante = models.CharField(max_length=20, blank=True)
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["aluno", "edicao"],
                condition=Q(status="ATIVA"),
                name="unica_inscricao_ativa_por_edicao",
            )
        ]

    def __str__(self):
        return f"{self.aluno.matricula} - {self.edicao} - {self.turma_codigo}"