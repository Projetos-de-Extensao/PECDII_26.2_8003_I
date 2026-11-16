from django.db import IntegrityError
from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Aluno, Inscricao


class AlunoAPITests(APITestCase):
    def setUp(self):
        self.aluno = Aluno.objects.create(
            matricula="2026001",
            nome="Ana Souza",
            email="ana@ibmec.edu.br",
            curso="Ciência de Dados e IA",
            campus="Botafogo",
        )

    def test_cria_aluno(self):
        resposta = self.client.post(
            "/alunos/",
            {
                "matricula": "2026002",
                "nome": "Bruno Lima",
                "email": "bruno@ibmec.edu.br",
                "curso": "Ciência de Dados e IA",
                "campus": "Botafogo",
            },
            format="json",
        )
        self.assertEqual(resposta.status_code, status.HTTP_201_CREATED)
        self.assertTrue(resposta.data["ativo"])  # default do model
        self.assertEqual(Aluno.objects.count(), 2)

    def test_nao_permite_matricula_duplicada(self):
        resposta = self.client.post(
            "/alunos/",
            {
                "matricula": "2026001",
                "nome": "Outra Pessoa",
                "email": "outra@ibmec.edu.br",
                "curso": "Direito",
                "campus": "Centro",
            },
            format="json",
        )
        self.assertEqual(resposta.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("matricula", resposta.data)

    def test_exclui_aluno_sem_inscricao(self):
        resposta = self.client.delete(f"/alunos/{self.aluno.id}/")
        self.assertEqual(resposta.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Aluno.objects.filter(id=self.aluno.id).exists())

    def test_bloqueia_exclusao_de_aluno_com_inscricao(self):
        Inscricao.objects.create(
            aluno=self.aluno,
            edicao="2026.2",
            turma_codigo="T01",
            disciplina="Engenharia de Software",
        )
        resposta = self.client.delete(f"/alunos/{self.aluno.id}/")
        self.assertEqual(resposta.status_code, status.HTTP_409_CONFLICT)
        self.assertIn("não pode ser excluído", resposta.data["detail"])
        self.assertTrue(Aluno.objects.filter(id=self.aluno.id).exists())


class InscricaoAPITests(APITestCase):
    def setUp(self):
        self.aluno = Aluno.objects.create(
            matricula="2026001",
            nome="Ana Souza",
            email="ana@ibmec.edu.br",
            curso="Ciência de Dados e IA",
            campus="Botafogo",
        )
        self.dados = {
            "aluno": self.aluno.id,
            "edicao": "2026.2",
            "turma_codigo": "T01",
            "disciplina": "Engenharia de Software",
        }

    def test_cria_inscricao_com_status_confirmada_e_nome_do_aluno(self):
        resposta = self.client.post("/inscricoes/", self.dados, format="json")
        self.assertEqual(resposta.status_code, status.HTTP_201_CREATED)
        self.assertEqual(resposta.data["status"], Inscricao.Status.CONFIRMADA)
        self.assertEqual(resposta.data["aluno_nome"], "Ana Souza")

    def test_nao_permite_duas_inscricoes_do_mesmo_aluno_na_mesma_edicao(self):
        self.client.post("/inscricoes/", self.dados, format="json")
        resposta = self.client.post("/inscricoes/", self.dados, format="json")
        self.assertEqual(resposta.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Inscricao.objects.count(), 1)

    def test_permite_mesmo_aluno_em_edicoes_diferentes(self):
        self.client.post("/inscricoes/", self.dados, format="json")
        resposta = self.client.post(
            "/inscricoes/", {**self.dados, "edicao": "2027.1"}, format="json"
        )
        self.assertEqual(resposta.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Inscricao.objects.count(), 2)

    def test_constraint_unica_tambem_vale_direto_no_banco(self):
        Inscricao.objects.create(aluno=self.aluno, edicao="2026.2",
                                 turma_codigo="T01", disciplina="ES")
        with self.assertRaises(IntegrityError):
            Inscricao.objects.create(aluno=self.aluno, edicao="2026.2",
                                     turma_codigo="T02", disciplina="ES")

    def test_rejeita_status_invalido(self):
        resposta = self.client.post(
            "/inscricoes/", {**self.dados, "status": "PENDENTE"}, format="json"
        )
        self.assertEqual(resposta.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("status", resposta.data)
