from django.core.management.base import BaseCommand
from django.db import transaction

from contas.models import Usuario

# Somente para desenvolvimento. Dados fictícios (RNF-07).
SENHA_DEV = 'tp-dev-2026'

USUARIOS = [
    {'username': 'aluno', 'first_name': 'Ana', 'last_name': 'Souza',
     'perfil': Usuario.Perfil.ALUNO, 'matricula': '202600001'},
    {'username': 'professor', 'first_name': 'Paulo', 'last_name': 'Lima',
     'perfil': Usuario.Perfil.PROFESSOR, 'matricula': 'SIAPE0001'},
    {'username': 'coordenacao', 'first_name': 'Carla', 'last_name': 'Mendes',
     'perfil': Usuario.Perfil.COORDENACAO, 'matricula': 'SIAPE0002'},
    {'username': 'admin', 'first_name': 'Alberto', 'last_name': 'Rocha',
     'perfil': Usuario.Perfil.ADMINISTRACAO, 'matricula': 'SIAPE0003',
     'is_staff': True, 'is_superuser': True},
]


class Command(BaseCommand):
    help = 'Cria usuários fictícios de cada perfil para desenvolvimento.'

    @transaction.atomic
    def handle(self, *args, **options):
        for dados in USUARIOS:
            dados = dict(dados)
            username = dados.pop('username')
            usuario, criado = Usuario.objects.update_or_create(
                username=username,
                defaults={**dados, 'email': f'{username}@exemplo.edu.br'},
            )
            usuario.set_password(SENHA_DEV)
            usuario.save()
            acao = 'criado' if criado else 'atualizado'
            self.stdout.write(f'{username} ({usuario.get_perfil_display()}) {acao}')
        self.stdout.write(self.style.SUCCESS(
            f'Seed concluído. Senha de todos os usuários: SENHA_DEV em {__name__}.'
        ))
