from django.contrib import admin

from .models import Inscricao


@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'edicao', 'turma', 'status', 'criado_em')
    search_fields = ('aluno__usuario__matricula', 'aluno__usuario__first_name', 'turma__codigo')
    list_filter = ('edicao', 'status')
    autocomplete_fields = ('aluno',)
    list_select_related = ('aluno__usuario', 'edicao', 'turma__disciplina')
