from rest_framework import serializers

from contas.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(source='get_full_name', read_only=True)
    perfil_display = serializers.CharField(source='get_perfil_display', read_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'nome', 'email', 'matricula', 'perfil', 'perfil_display']
        read_only_fields = fields
