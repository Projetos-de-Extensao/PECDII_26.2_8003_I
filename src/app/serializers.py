from rest_framework import serializers

from app.models import Aluno, Inscricao, Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco', 'descricao', 'disponivel']
        read_only_fields = ['id']


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'matricula', 'nome', 'email', 'curso', 'campus', 'ativo']
        read_only_fields = ['id']


class InscricaoSerializer(serializers.ModelSerializer):
    # Mostra o nome do aluno na resposta, sem precisar de outra consulta na API
    aluno_nome = serializers.CharField(source='aluno.nome', read_only=True)

    class Meta:
        model = Inscricao
        fields = [
            'id',
            'aluno',
            'aluno_nome',
            'edicao',
            'turma_codigo',
            'disciplina',
            'status',
            'criado_em',
        ]
        read_only_fields = ['id', 'criado_em']