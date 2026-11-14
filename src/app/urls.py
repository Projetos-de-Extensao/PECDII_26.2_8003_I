from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app.views import AlunoViewSet, InscricaoViewSet, ProdutoViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet, basename='produto')
router.register(r'alunos', AlunoViewSet, basename='aluno')
router.register(r'inscricoes', InscricaoViewSet, basename='inscricao')

urlpatterns = [
    path('', include(router.urls)),
]