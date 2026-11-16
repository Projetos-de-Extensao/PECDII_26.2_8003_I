"""Cria os grupos de acesso ao admin para os atores do sistema.

- Secretaria: cadastra, edita, exclui e consulta alunos e inscrições.
- Coordenação: apenas consulta alunos e inscrições.

Para dar acesso a alguém, no admin: Usuários -> marcar "Membro da equipe"
e adicionar o usuário ao grupo correspondente.
"""

from django.contrib.auth.management import create_permissions
from django.db import migrations

MODELOS = ["aluno", "inscricao"]

GRUPOS = {
    "Secretaria": ["add", "change", "delete", "view"],
    "Coordenação": ["view"],
}


def criar_grupos(apps, schema_editor):
    # As permissões normalmente só são criadas depois de todas as migrations.
    # Forçamos a criação aqui para conseguir associá-las aos grupos.
    app_config = apps.get_app_config("app")
    app_config.models_module = True
    create_permissions(app_config, apps=apps, verbosity=0)
    app_config.models_module = None

    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")

    for nome, acoes in GRUPOS.items():
        grupo, _ = Group.objects.get_or_create(name=nome)
        codenames = [f"{acao}_{modelo}" for acao in acoes for modelo in MODELOS]
        permissoes = Permission.objects.filter(
            content_type__app_label="app", codename__in=codenames
        )
        grupo.permissions.set(permissoes)


def remover_grupos(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(name__in=GRUPOS.keys()).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_delete_produto"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.RunPython(criar_grupos, remover_grupos),
    ]
