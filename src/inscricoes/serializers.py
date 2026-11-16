from rest_framework import serializers

from inscricoes.models import Inscricao


class InscricaoSerializer(serializers.ModelSerializer):
    # Mostra nomes legíveis na resposta, sem precisar de outra consulta na API.
    aluno_nome = serializers.CharField(source='aluno.nome', read_only=True)
    edicao_semestre = serializers.CharField(source='edicao.semestre', read_only=True)
    turma_codigo = serializers.CharField(source='turma.codigo', read_only=True)
    disciplina = serializers.CharField(source='turma.disciplina.nome', read_only=True)

    class Meta:
        model = Inscricao
        fields = [
            'id', 'aluno', 'aluno_nome', 'edicao', 'edicao_semestre',
            'turma', 'turma_codigo', 'disciplina', 'status', 'criado_em',
        ]
        read_only_fields = ['id', 'criado_em']
