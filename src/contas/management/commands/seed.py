from datetime import date, datetime
from zoneinfo import ZoneInfo

from django.core.management.base import BaseCommand
from django.db import transaction

from academico.models import Aluno, Curso, Disciplina, Turma
from contas.models import Usuario
from edicoes.models import Campus, Edicao

FUSO = ZoneInfo('America/Sao_Paulo')

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
        self.criar_dados_academicos()
        self.stdout.write(self.style.SUCCESS(
            f'Seed concluído. Senha de todos os usuários: SENHA_DEV em {__name__}.'
        ))

    def criar_dados_academicos(self):
        """Curso, campus, turma e edição fictícios, e o vínculo do usuário 'aluno'."""
        curso, _ = Curso.objects.get_or_create(codigo='CDIA', defaults={'nome': 'Ciência de Dados e IA'})
        campus, _ = Campus.objects.get_or_create(nome='Botafogo')
        disciplina, _ = Disciplina.objects.get_or_create(
            codigo='IBM8936', defaults={'nome': 'Projeto de Extensão'},
        )
        Turma.objects.get_or_create(
            codigo='8003', semestre='2026.2',
            defaults={'disciplina': disciplina, 'professor': Usuario.objects.get(username='professor')},
        )
        edicao, _ = Edicao.objects.get_or_create(
            semestre='2026.2',
            defaults={
                'data_prova': date(2026, 11, 28),
                'inicio_inscricao': datetime(2026, 11, 1, 8, 0, tzinfo=FUSO),
                'fim_inscricao': datetime(2026, 11, 20, 23, 59, tzinfo=FUSO),
                'status': Edicao.Status.INSCRICOES_ABERTAS,
            },
        )
        edicao.campi.add(campus)
        edicao.cursos.add(curso)
        Aluno.objects.get_or_create(
            usuario=Usuario.objects.get(username='aluno'),
            defaults={'curso': curso, 'campus': campus},
        )
        self.stdout.write('dados acadêmicos (curso, campus, turma, edição 2026.2) prontos')
