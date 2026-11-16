from django.contrib import admin

from .models import Aluno, Curso, Disciplina, Turma


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome')
    search_fields = ('codigo', 'nome')


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome')
    search_fields = ('codigo', 'nome')


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'semestre', 'disciplina', 'professor')
    search_fields = ('codigo', 'disciplina__nome')
    list_filter = ('semestre',)
    list_select_related = ('disciplina', 'professor')


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'curso', 'campus', 'ativo')
    search_fields = ('usuario__matricula', 'usuario__first_name', 'usuario__last_name', 'usuario__email')
    list_filter = ('campus', 'curso', 'ativo')
    list_select_related = ('usuario', 'curso', 'campus')
