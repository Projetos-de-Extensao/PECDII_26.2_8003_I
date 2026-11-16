from datetime import date, datetime, timezone

from django.db import IntegrityError
from django.test import TestCase

from academico.models import Aluno, Curso, Disciplina, Turma
from contas.models import Usuario
from edicoes.models import Campus, Edicao
from inscricoes.models import Inscricao


class InscricaoModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        usuario = Usuario.objects.create_user(
            username='ana', first_name='Ana', last_name='Souza',
            matricula='202600001', perfil=Usuario.Perfil.ALUNO,
        )
        cls.aluno = Aluno.objects.create(
            usuario=usuario,
            curso=Curso.objects.create(codigo='CDIA', nome='Ciência de Dados e IA'),
            campus=Campus.objects.create(nome='Botafogo'),
        )
        disciplina = Disciplina.objects.create(codigo='IBM8936', nome='Projeto de Extensão')
        cls.turma = Turma.objects.create(codigo='8003', semestre='2026.2', disciplina=disciplina)
        cls.edicao = Edicao.objects.create(
            semestre='2026.2',
            data_prova=date(2026, 11, 28),
            inicio_inscricao=datetime(2026, 11, 1, tzinfo=timezone.utc),
            fim_inscricao=datetime(2026, 11, 20, tzinfo=timezone.utc),
        )

    def test_dados_do_aluno_vem_do_usuario(self):
        self.assertEqual(self.aluno.matricula, '202600001')
        self.assertEqual(self.aluno.nome, 'Ana Souza')

    def test_inscricao_liga_aluno_edicao_e_turma(self):
        inscricao = Inscricao.objects.create(aluno=self.aluno, edicao=self.edicao, turma=self.turma)
        self.assertEqual(inscricao.status, Inscricao.Status.CONFIRMADA)
        self.assertEqual(inscricao.turma.disciplina.codigo, 'IBM8936')

    def test_rn01_aluno_so_tem_uma_inscricao_por_edicao(self):
        Inscricao.objects.create(aluno=self.aluno, edicao=self.edicao, turma=self.turma)
        with self.assertRaises(IntegrityError):
            Inscricao.objects.create(aluno=self.aluno, edicao=self.edicao, turma=self.turma)
