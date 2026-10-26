from django.contrib import admin

from .models import Aluno, Inscricao, Produto

admin.site.register(Produto)


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("matricula", "nome", "curso", "campus", "ativo")
    search_fields = ("matricula", "nome", "email")
    list_filter = ("campus", "curso", "ativo")


@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ("aluno", "edicao", "turma_codigo", "disciplina", "status")
    search_fields = ("aluno__matricula", "aluno__nome", "turma_codigo")
    list_filter = ("edicao", "status")
    autocomplete_fields = ("aluno",)