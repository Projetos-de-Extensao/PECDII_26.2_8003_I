# Sistema do Teste de Progresso

**Código da Disciplina**: IBM8936<br>

## Sobre

Sistema para organizar o Teste de Progresso: inscrição do aluno com escolha da
turma que recebe o bônus, ensalamento e escala de aplicadores, presença, notas
e exportação do bônus. A documentação completa (requisitos, casos de uso e
plano de construção) está em `docs/` e é publicada com MkDocs.

## Arquitetura

| Parte | Pasta | Tecnologias |
|---|---|---|
| API REST | `src/` | Python, Django, Django REST Framework, JWT, Swagger |
| Front-end | `frontend/` | React, Vite, React Router |
| Documentação | `docs/` | MkDocs Material |

## Como rodar

Pré-requisitos: Python 3.14 e Node.js 22.

### API (porta 8000)

```bash
python -m venv .venv-1
source .venv-1/bin/activate
pip install -r requirements.txt
cd src
python manage.py migrate
python manage.py seed        # usuários fictícios: aluno, professor, coordenacao, admin
python manage.py runserver
```

A senha dos usuários do `seed` está em `src/contas/management/commands/seed.py`
(`SENHA_DEV`) e serve só para desenvolvimento.

- Swagger: <http://127.0.0.1:8000/api/v1/docs/>
- Admin do Django: <http://127.0.0.1:8000/admin/>

### Front-end (porta 5173)

```bash
cd frontend
cp .env.example .env
npm install
npm run dev
```

Acesse <http://127.0.0.1:5173> e entre com um dos usuários do `seed`.

### Testes

```bash
cd src && python manage.py test
cd frontend && npm test
```

### Documentação (porta 8001)

```bash
mkdocs serve -a 127.0.0.1:8001
```
