from rest_framework import serializers

from academico.models import Aluno


class AlunoSerializer(serializers.ModelSerializer):
    # Nome, matrícula e e-mail vêm do Usuario ligado ao aluno.
    matricula = serializers.CharField(read_only=True)
    nome = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    curso_nome = serializers.CharField(source='curso.nome', read_only=True)
    campus_nome = serializers.CharField(source='campus.nome', read_only=True)

    class Meta:
        model = Aluno
        fields = [
            'id', 'usuario', 'matricula', 'nome', 'email',
            'curso', 'curso_nome', 'campus', 'campus_nome', 'ativo',
        ]
        read_only_fields = ['id']
