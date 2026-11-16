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
