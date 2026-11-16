from django.db import models


# Exemplo didático do guia EchoAPI. As classes do sistema ficam nos apps do domínio
# (academico, edicoes, inscricoes...).
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
