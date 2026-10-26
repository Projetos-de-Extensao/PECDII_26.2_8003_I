from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from contas.models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'perfil', 'matricula', 'is_active']
    list_filter = ['perfil', 'is_active', 'is_staff']
    search_fields = ['username', 'first_name', 'last_name', 'email', 'matricula']
    fieldsets = UserAdmin.fieldsets + (
        ('Perfil institucional', {'fields': ['perfil', 'matricula']}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Perfil institucional', {'fields': ['perfil', 'matricula']}),
    )
