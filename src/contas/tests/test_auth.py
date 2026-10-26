from django.test import override_settings
from django.urls import path
from rest_framework.response import Response
from rest_framework.test import APITestCase
from rest_framework.views import APIView

from contas.models import Usuario
from contas.permissions import IsAdministracao, IsAluno

SENHA = 'senha-de-teste-123'


class SomenteAluno(APIView):
    permission_classes = [IsAluno]

    def get(self, request):
        return Response({'ok': True})


class SomenteAdministracao(APIView):
    permission_classes = [IsAdministracao]

    def get(self, request):
        return Response({'ok': True})


urlpatterns = [
    path('aluno/', SomenteAluno.as_view()),
    path('administracao/', SomenteAdministracao.as_view()),
]


def criar_usuario(username, perfil):
    return Usuario.objects.create_user(username=username, password=SENHA, perfil=perfil)


class AutenticacaoTests(APITestCase):
    """UC01 · RF-01: login por credencial e identificação do perfil."""

    def setUp(self):
        self.aluno = criar_usuario('aluno', Usuario.Perfil.ALUNO)

    def obter_token(self, username, senha):
        return self.client.post('/api/v1/auth/token/', {'username': username, 'password': senha})

    def test_login_valido_retorna_tokens(self):
        resposta = self.obter_token('aluno', SENHA)
        self.assertEqual(resposta.status_code, 200)
        self.assertIn('access', resposta.data)
        self.assertIn('refresh', resposta.data)

    def test_login_com_senha_errada_e_recusado(self):
        resposta = self.obter_token('aluno', 'errada')
        self.assertEqual(resposta.status_code, 401)

    def test_me_retorna_perfil_do_usuario(self):
        token = self.obter_token('aluno', SENHA).data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        resposta = self.client.get('/api/v1/auth/me/')
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.data['username'], 'aluno')
        self.assertEqual(resposta.data['perfil'], 'aluno')

    def test_me_exige_autenticacao(self):
        resposta = self.client.get('/api/v1/auth/me/')
        self.assertEqual(resposta.status_code, 401)

    def test_refresh_gera_novo_access(self):
        refresh = self.obter_token('aluno', SENHA).data['refresh']
        resposta = self.client.post('/api/v1/auth/token/refresh/', {'refresh': refresh})
        self.assertEqual(resposta.status_code, 200)
        self.assertIn('access', resposta.data)


@override_settings(ROOT_URLCONF=__name__)
class PermissaoPorPerfilTests(APITestCase):
    """RF-02: cada perfil acessa apenas o que lhe cabe."""

    def test_aluno_acessa_rota_de_aluno(self):
        self.client.force_authenticate(criar_usuario('a', Usuario.Perfil.ALUNO))
        self.assertEqual(self.client.get('/aluno/').status_code, 200)

    def test_aluno_nao_acessa_rota_da_administracao(self):
        self.client.force_authenticate(criar_usuario('a', Usuario.Perfil.ALUNO))
        self.assertEqual(self.client.get('/administracao/').status_code, 403)

    def test_professor_nao_acessa_rota_de_aluno(self):
        self.client.force_authenticate(criar_usuario('p', Usuario.Perfil.PROFESSOR))
        self.assertEqual(self.client.get('/aluno/').status_code, 403)

    def test_anonimo_nao_acessa(self):
        self.assertEqual(self.client.get('/aluno/').status_code, 401)
