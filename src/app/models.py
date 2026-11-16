from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    matricula = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    curso = models.CharField(max_length=100)
    campus = models.CharField(max_length=80)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

    def __str__(self):
        return f"{self.matricula} - {self.nome}"


class Inscricao(models.Model):
    class Status(models.TextChoices):
        CONFIRMADA = "CONFIRMADA", "Confirmada"
        CANCELADA = "CANCELADA", "Cancelada"

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.PROTECT,
        related_name="inscricoes",
    )
    edicao = models.CharField(max_length=20)
    turma_codigo = models.CharField(max_length=20)
    disciplina = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.CONFIRMADA,
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criado_em"]
        verbose_name = "Inscrição"
        verbose_name_plural = "Inscrições"
        constraints = [
            models.UniqueConstraint(
                fields=["aluno", "edicao"],
                name="uniq_inscricao_aluno_edicao",
            )
        ]

    def __str__(self):
        return f"{self.aluno.matricula} - {self.edicao}"