from django.contrib import admin

from .models import Campus, Edicao


@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    search_fields = ('nome',)


@admin.register(Edicao)
class EdicaoAdmin(admin.ModelAdmin):
    list_display = ('semestre', 'data_prova', 'inicio_inscricao', 'fim_inscricao', 'status')
    list_filter = ('status',)
    filter_horizontal = ('campi', 'cursos')
