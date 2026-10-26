---
id: plano_construcao
title: Plano de Construção
---

# Plano de Construção — Sistema do Teste de Progresso

## Objetivo

Transformar os artefatos da Elaboração (requisitos RF-01 a RF-34, casos de uso
UC01 a UC15, regras RN01 a RN19, diagrama de classes e protótipos) em uma
**API REST em Django** e um **front-end React separado** que a consome,
entregues em incrementos curtos e rastreáveis.

```text
Navegador ──► Front-end React (Vite)  ──HTTP/JSON + JWT──►  API Django REST  ──► Banco
              frontend/                                     src/
```

## Decisões técnicas

| Tema | Decisão | Motivo |
|---|---|---|
| Back-end | Python + Django 6.1 + Django REST Framework | Já adotado no repositório e na disciplina. |
| Contrato da API | Endpoints em `/api/v1/`, documentados com OpenAPI/Swagger (`drf-spectacular`) em `/api/docs/` | O front-end e o EchoAPI usam a mesma documentação. |
| Front-end | React + Vite (JavaScript) + React Router, em `frontend/` | Projeto separado, como pedido; Vite dá servidor de desenvolvimento rápido. |
| Chamadas HTTP | Um único cliente (`frontend/src/api/`) com `fetch` e o token no cabeçalho | Centraliza URL base, token e tratamento de erros. |
| Autenticação | Usuário customizado com campo `perfil` + JWT (`djangorestframework-simplejwt`) | Atende RF-01 e RF-02 sem sessão compartilhada; SSO fica como evolução. |
| Autorização | Permissões do DRF por perfil (aluno, professor, coordenação, administração) | O front-end só esconde menus; quem garante o acesso é a API (RN17). |
| CORS | `django-cors-headers` liberando a origem do front-end | Front e API rodam em portas diferentes (5173 e 8000). |
| Banco | SQLite em desenvolvimento | Zero configuração; o ORM permite trocar por PostgreSQL na Transição. |
| Integração acadêmica | Upload de CSV pelo front-end para endpoints de importação; exportação como download | Definido no UC06 e RF-27 (sem integração em tempo real). |
| PDFs | Gerados pela API e baixados pelo front-end | Mapa de sala, lista de presença, etiqueta de porta e comprovante. |
| Testes | Back-end: `APITestCase`, um teste por regra de negócio e por permissão. Front-end: Vitest + Testing Library nos fluxos principais | As RNs são o núcleo do sistema; os testes de API garantem o contrato. |
| CI | GitHub Actions com dois jobs: `python manage.py test` e `npm run build && npm test` | Ver [GitHub Workflows](github_workflows.md). |

## Organização do código

Hoje o repositório tem dois projetos Django: `setup/` na raiz e `src/project/`
(com DRF e o exemplo `Produto`). A proposta é **concentrar o
sistema em `src/`**, mantendo o app `app` (Produto) apenas como exemplo do guia
do EchoAPI, e criar um app Django por área do domínio:

```text
src/
├── project/          # settings, urls raiz
├── contas/           # Usuario (perfil), login, permissões         UC01
├── academico/        # Curso, Disciplina, Turma, Matricula,
│                     # Aluno, Professor, importação CSV            UC06
├── edicoes/          # Edicao, RegraBonus, Campus, Sala,
│                     # Disponibilidade                             UC05, UC07
├── inscricoes/       # Inscricao, AtendimentoEspecial,
│                     # Consentimento, comprovante                  UC02, UC03, UC04, UC15
├── logistica/        # Alocacao, Escala, Material, documentos PDF  UC08, UC09, UC13
├── notas/            # Presenca, LoteNotas, Nota, Bonus, exportação UC10, UC11, UC12
├── relatorios/       # indicadores agregados                       UC14
└── auditoria/        # RegistroAuditoria (quem, quando, antes, depois) RF-33, RN13, RN18
```

Cada app do back-end segue o mesmo padrão: `models.py`, `services.py` (regras
de negócio), `serializers.py`, `permissions.py`, `views.py` (ViewSets) e
`tests/`.

O front-end fica em uma pasta própria na raiz do repositório:

```text
frontend/
├── package.json
├── vite.config.js
├── .env.example          # VITE_API_URL=http://127.0.0.1:8000/api/v1
└── src/
    ├── api/              # cliente HTTP e uma função por endpoint
    ├── auth/             # login, armazenamento do token, rota protegida por perfil
    ├── components/       # layout, menu por perfil, tabelas, formulários
    └── pages/
        ├── aluno/        # painel, inscrição, minha inscrição, meus dados
        ├── professor/    # escala, espelho de notas
        ├── coordenacao/  # indicadores
        └── admin/        # edições, importações, salas, ensalamento, presença, notas
```

!!! warning "Antes da primeira migração"
    O modelo de usuário customizado (`AUTH_USER_MODEL = "contas.Usuario"`)
    precisa existir **antes** de rodar `migrate` pela primeira vez. Por isso
    o banco `src/db.sqlite3` foi recriado na Sprint 0 e deixou de ser versionado: cada pessoa roda `migrate` e `seed`.

## Modelo de dados (especificação inicial)

| Classe | Atributos principais | Relacionamentos |
|---|---|---|
| `Usuario` | matrícula/SIAPE, nome, e-mail, perfil | 1–1 com `Aluno` ou `Professor` |
| `Curso` | código, nome | 1–N `Aluno` |
| `Disciplina` | código, nome | 1–N `Turma` |
| `Turma` | código, semestre | N–1 `Disciplina`, N–1 `Professor` |
| `Matricula` | semestre, situação | `Aluno` N–N `Turma` |
| `Edicao` | semestre, data, horário, início e fim da inscrição, status | N–N `Campus`, N–N `Curso`, 1–1 `RegraBonus` |
| `RegraBonus` | nota mínima e máxima brutas, bônus máximo (≤ 1) | — |
| `Campus` / `Sala` | capacidade nominal, capacidade de prova, acessível | `Campus` 1–N `Sala` |
| `Inscricao` | número do comprovante, status, data | N–1 `Aluno`, `Edicao`, `Turma`; única por aluno e edição (RN01) |
| `AtendimentoEspecial` | descrição, consentimento, deferido | 1–1 `Inscricao`, acesso restrito (RN04) |
| `Alocacao` | — | `Inscricao` → `Sala` |
| `Escala` | função (aplicador/reserva) | `Professor` → `Sala` na `Edicao` |
| `Presenca` | presente | 1–1 `Inscricao` |
| `Nota` | nota bruta, bônus, status (válida/bloqueada/exportada) | 1–1 `Inscricao` |
| `RegistroAuditoria` | autor, data, entidade, campo, valor anterior, valor novo, justificativa | genérico |

As regras de negócio ficam em **serviços** (`services.py` de cada app), não nas
views, para poderem ser testadas isoladamente. O front-end **nunca** repete
uma regra de negócio: ele exibe os erros de validação devolvidos pela API.

## Forma de trabalho por funcionalidade

Cada item das sprints abaixo é entregue em duas partes, nesta ordem:

1. **API:** modelo, serviço, serializer, endpoint, permissão e testes. O
   endpoint é conferido no Swagger ou no EchoAPI.
2. **Tela:** página React que consome o endpoint, conferida com o protótipo.

Assim o grupo pode dividir o trabalho entre back-end e front-end, desde que o
contrato do endpoint esteja definido antes.

## Plano por sprint

As sprints seguem os registros em `Iteração/` e a prioridade MoSCoW da
pesquisa (M = obrigatório, S = desejável, C = opcional). O **MVP** é o
conjunto de todos os requisitos M.

### Sprint 0 — Fundação

- [x] Escolher `src/` como projeto único e remover o projeto duplicado `setup/` da raiz.
- [x] Criar os apps acima e registrar em `INSTALLED_APPS`.
- [x] `contas.Usuario` customizado; `LANGUAGE_CODE = "pt-br"`, `TIME_ZONE = "America/Sao_Paulo"`.
- [x] Mover `SECRET_KEY` e `DEBUG` para variáveis de ambiente.
- [x] Instalar e configurar `djangorestframework-simplejwt`, `django-cors-headers` e `drf-spectacular`.
- [x] Endpoints de token (`/api/v1/auth/token/`, `/refresh/`) e `/api/v1/auth/me/` com o perfil do usuário.
- [x] Criar `frontend/` com Vite + React, React Router e o cliente HTTP.
- [x] Layout base do protótipo, tela de login e menu por perfil.
- [x] Workflow de CI com os jobs do back-end e do front-end.
- [x] Comando `seed` com dados fictícios (RNF-07).
- [x] `.claude/launch.json` e README com os dois comandos de execução (`runserver` e `npm run dev`).

**Pronto quando:** API e front-end sobem juntos, o login pelo React funciona para cada perfil do `seed` e a CI está verde.

### Sprint 1 — Cadastros base e autenticação (UC01, UC05, UC06, UC07)

- [ ] Logout, renovação do token e redirecionamento ao painel do perfil (RF-01, RF-02).
- [ ] Modelos, serializers e endpoints de `academico` e `edicoes`, com permissões por perfil.
- [ ] Importação CSV de alunos, disciplinas, turmas e matrículas com relatório de erros (RF-03).
- [ ] CRUD de edição, regra de bônus e período de inscrição (RF-05 a RF-07).
- [ ] CRUD de campus, salas e disponibilidade de professores (RF-15, RF-16).
- [ ] Trilha de auditoria genérica (base para RF-33).

**Pronto quando:** a administração consegue montar uma edição completa a partir de CSVs.

### Sprint 2 — Inscrição do aluno (UC02, UC03, UC04) — núcleo do MVP

- [ ] Painel do aluno com a edição vigente e o status (Tela 02).
- [ ] Fluxo de inscrição em etapas: turma elegível → atendimento especial → revisão → comprovante (Telas 03 a 07).
- [ ] Regras RN01 a RN06 em `inscricoes/services.py`, com testes para os fluxos A1 a A7.
- [ ] Alterar ou cancelar dentro do prazo (RF-13).
- [ ] E-mail de confirmação via backend de console em desenvolvimento (RF-14); falha não desfaz a inscrição (A7).
- [ ] Coleção do EchoAPI com os endpoints de inscrição, atualizando o guia [EchoAPI](echo_api.md).

**Pronto quando:** um aluno do `seed` se inscreve, recebe comprovante e todos os testes de RN passam.

### Sprint 3 — Ensalamento e escala (UC08, UC09, UC13)

- [ ] Algoritmo de ensalamento: agrupar por campus, reservar salas acessíveis, distribuir sem exceder a capacidade de prova (RN07 a RN09, RN12).
- [ ] Escala de aplicadores e reservas sem conflito de horário (RN10, RN11).
- [ ] Cálculo de materiais com margem de reserva (RF-20).
- [ ] Validação que bloqueia a publicação (A1 a A4) e alerta de capacidade (RF-23).
- [ ] Ajuste manual com justificativa auditada (UC09, RN13).
- [ ] PDFs: mapa de sala, lista de presença, etiqueta de porta (RF-21).
- [ ] "Onde faço prova" para o aluno e escala para o professor (RF-22, UC13).

**Pronto quando:** o `seed` gera um ensalamento válido e publicável, com os PDFs.

### Sprint 4 — Presença, notas e bônus (UC10, UC11, UC12)

- [ ] Registro de presença por sala (RF-24).
- [ ] Importação de notas brutas com validação de formato, matrícula e faixa (A1 a A3).
- [ ] Conversão para bônus de 0 a 1 e bloqueio de ausentes (RF-25, RF-28, RN14, RN15).
- [ ] Vínculo do bônus à turma escolhida e espelho do professor restrito às suas turmas (RF-26, RN16, RN17).
- [ ] Exportação CSV somente de registros válidos e confirmados (RF-27, RN19).
- [ ] Alteração de nota publicada com auditoria completa (RF-33, RN18).

**Pronto quando:** o ciclo inscrição → presença → nota → exportação roda de ponta a ponta.

### Sprint 5 — Autoatendimento e indicadores (UC14, UC15)

- [ ] "Meus dados" com exportação CSV/PDF e revogação do consentimento (RF-32, LGPD).
- [ ] Painel de indicadores: adesão, ocupação e desempenho agregados, com a coordenação limitada ao próprio curso (RF-29 a RF-31).
- [ ] Requisitos S restantes: comprovante em PDF, exceções manuais (RF-04), clonar edição (RF-08).

**Pronto quando:** todos os requisitos M e S estão implementados.

### Sprint 6 — Transição

- [ ] Testes de aceitação guiados pelos casos de uso, com a turma/stakeholders.
- [ ] Revisão de segurança: permissões por perfil, dado sensível restrito, `DEBUG=False`.
- [ ] Deploy da API (PostgreSQL + servidor de aplicação) e do front-end (build estático do Vite), com CORS restrito ao domínio final.
- [ ] Manual de uso.
- [ ] Opcional: comparativo entre edições (RF-34).

## Rastreabilidade sprint × requisitos

| Sprint | Casos de uso | Requisitos |
|---|---|---|
| 0 | — | RNF, infraestrutura |
| 1 | UC01, UC05, UC06, UC07 | RF-01 a RF-03, RF-05 a RF-07, RF-15, RF-16 |
| 2 | UC02, UC03, UC04 | RF-09 a RF-14 |
| 3 | UC08, UC09, UC13 | RF-17 a RF-23 |
| 4 | UC10, UC11, UC12 | RF-24 a RF-28, RF-33 |
| 5 | UC14, UC15 | RF-04, RF-08, RF-29 a RF-32 |
| 6 | todos | RF-34, RNF |

## Definição de pronto (para toda tarefa)

1. Código em branch própria com Pull Request revisado por outro membro.
2. Testes de API das regras de negócio e das permissões envolvidas, passando na CI.
3. Endpoint documentado no Swagger.
4. Tela React conferida com o protótipo, exibindo os erros devolvidos pela API.
5. Issue correspondente fechada no [GitHub Projects](github_projects.md).

## Versionamento

| Data | Versão | Descrição |
|---|---|---|
| 26/10/2026 | 1.0 | Criação do plano de construção. |
| 26/10/2026 | 1.1 | Front-end React separado consumindo a API REST com JWT. |
| 26/10/2026 | 1.2 | Sprint 0 concluída. |
