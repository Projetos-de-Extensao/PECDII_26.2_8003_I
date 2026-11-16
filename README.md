# Projeto Back-End 

**Código da Disciplina**: IBM8936<br>

## Sobre 
Descreva o seu projeto em linhas gerais. 

## Instalação 
**Linguagens**: Python, Django<br>
**Tecnologias**: Github, Visual Studio Code<br>
 os pré-requisitos para rodar o seu projeto são UX, Engenharia de Dados, POO.


## Como rodar

O projeto Django fica na pasta `src/` (configurações em `src/project/`, app em `src/app/`).

```bash
pip install -r requirements.txt
cd src
python manage.py migrate
python manage.py runserver
```

- API: `http://127.0.0.1:8000/` (rotas `alunos/`, `inscricoes/`, `produtos/`)
- Swagger: `http://127.0.0.1:8000/api/docs/`
- Testes: `python manage.py test` (dentro de `src/`)

O `db.sqlite3` não é versionado — cada um gera o seu com `migrate`.

## Perfis de acesso ao admin

O `migrate` cria dois grupos automaticamente:

| Grupo | O que pode fazer em `/admin/` |
|---|---|
| **Secretaria** | Cadastrar, editar, excluir e consultar alunos e inscrições |
| **Coordenação** | Apenas consultar alunos e inscrições |

Para dar acesso a alguém: entre no admin com um superusuário → **Usuários** → crie ou abra o usuário → marque **Membro da equipe** → em **Grupos**, adicione *Secretaria* ou *Coordenação* → salve.
