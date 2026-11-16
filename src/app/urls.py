from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app.views import AlunoViewSet, InscricaoViewSet

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet, basename='aluno')
router.register(r'inscricoes', InscricaoViewSet, basename='inscricao')

urlpatterns = [
    path('', include(router.urls)),
]