# Brainstorm — Parte 1

## Tema
**Teste de Progresso — Inscrição e escolha da disciplina**

## Introdução

<p align="justify">
Esta etapa do brainstorm teve como objetivo discutir as funcionalidades relacionadas ao acesso do aluno ao sistema, sua inscrição no Teste de Progresso e a escolha da disciplina na qual será aplicado o bônus obtido na avaliação.
</p>

## Perguntas

### 1. Qual deve ser o principal objetivo da aplicação?

<p align="justify">

<b>Integrante 1</b> - A aplicação deve centralizar todo o processo relacionado ao Teste de Progresso, evitando a utilização de diferentes planilhas e trocas de e-mails.

<b>Integrante 2</b> - O sistema deve permitir que o aluno faça sua inscrição no Teste de Progresso e escolha em qual disciplina deseja receber a nota bônus.

<b>Integrante 3</b> - A plataforma deve automatizar processos administrativos e logísticos, reduzindo erros e retrabalho.

</p>

---

### 2. Como deverá funcionar o processo de inscrição do aluno?

<p align="justify">

<b>Integrante 1</b> - O aluno deverá acessar o sistema utilizando sua credencial institucional e visualizar as edições disponíveis do Teste de Progresso.

<b>Integrante 2</b> - A inscrição somente deverá ser permitida durante o período definido pela instituição.

<b>Integrante 3</b> - Após finalizar a inscrição, o aluno deverá receber uma confirmação e poderá consultar posteriormente as informações cadastradas.

</p>

---

### 3. Como deverá funcionar a escolha da disciplina que receberá a nota?

<p align="justify">

<b>Integrante 1</b> - O sistema deverá apresentar somente as disciplinas nas quais o aluno esteja matriculado no semestre atual.

<b>Integrante 2</b> - O aluno deverá selecionar uma disciplina para receber o bônus obtido no Teste de Progresso.

<b>Integrante 3</b> - A escolha deverá ficar vinculada à inscrição e poderá ser alterada enquanto o período de inscrição estiver aberto.

</p>

## Requisitos elicitados

| ID | Descrição |
|---|---|
| BS01 | O sistema deve permitir autenticação utilizando credencial institucional. |
| BS02 | O sistema deve possuir diferentes perfis de acesso. |
| BS03 | O sistema deve permitir a criação de edições do Teste de Progresso. |
| BS04 | O sistema deve permitir configurar o período de abertura e fechamento das inscrições. |
| BS05 | O aluno deve poder realizar sua inscrição em uma edição aberta. |
| BS06 | O aluno deve escolher a disciplina que receberá a nota bônus. |
| BS07 | O sistema deve apresentar apenas disciplinas nas quais o aluno esteja matriculado. |
| BS08 | O aluno deve poder alterar ou cancelar sua inscrição enquanto o período estiver aberto. |
| BS09 | O sistema deve disponibilizar uma confirmação ou comprovante de inscrição. |

## Conclusão

<p align="justify">
A primeira parte do brainstorm permitiu identificar os requisitos relacionados à entrada do aluno no sistema, ao processo de inscrição e à seleção da disciplina responsável por receber o bônus do Teste de Progresso.
</p>


# Brainstorm — Parte 3

## Tema

**Teste de Progresso — Notas, segurança e relatórios**

## Introdução

<p align="justify">
Esta etapa do brainstorm teve como foco os processos posteriores à organização da prova, envolvendo presença dos alunos, lançamento e consulta das notas, disponibilização das informações para cada usuário, proteção de dados e geração de relatórios administrativos.
</p>

## Perguntas

### 7. Como deverá funcionar o lançamento e a consulta das notas?

<p align="justify">

<b>Integrante 1</b> - Após a realização do teste, as notas deverão ser importadas para o sistema e convertidas para a escala de bônus utilizada pela instituição.

<b>Integrante 2</b> - A nota deverá ser vinculada automaticamente à disciplina escolhida pelo aluno durante sua inscrição.

<b>Integrante 3</b> - Alunos ausentes não deverão receber o bônus e alterações realizadas nas notas deverão ser registradas.

</p>

---

### 8. Quais informações serão importantes para cada usuário?

<p align="justify">

<b>Integrante 1</b> - O aluno deverá conseguir consultar sua inscrição, disciplina escolhida, data, campus, sala e resultado.

<b>Integrante 2</b> - O professor deverá visualizar os alunos que escolheram suas disciplinas e as respectivas notas.

<b>Integrante 3</b> - A coordenação e a Pró-Reitoria deverão possuir informações consolidadas sobre inscrições, ocupação das salas, professores e desempenho.

</p>

---

### 9. Como o sistema deverá tratar acessibilidade e dados pessoais?

<p align="justify">

<b>Integrante 1</b> - Durante a inscrição, o aluno deverá conseguir solicitar atendimento especial quando necessário.

<b>Integrante 2</b> - Informações relacionadas a atendimento especial deverão possuir acesso restrito.

<b>Integrante 3</b> - O sistema deverá coletar somente os dados necessários e limitar o acesso às informações de acordo com o perfil de cada usuário.

</p>

---

### 10. Quais relatórios seriam importantes para a instituição?

<p align="justify">

<b>Integrante 1</b> - Relatórios de quantidade de inscritos por curso, período e campus.

<b>Integrante 2</b> - Relatórios de ocupação das salas e professores responsáveis pela aplicação.

<b>Integrante 3</b> - Relatórios de notas e desempenho consolidado, permitindo acompanhar a evolução dos estudantes entre diferentes aplicações do Teste de Progresso.

</p>

## Requisitos elicitados

| ID   | Descrição                                                                                       |
| ---- | ----------------------------------------------------------------------------------------------- |
| BS24 | O sistema deve permitir registrar presença e ausência dos alunos.                               |
| BS25 | O sistema deve permitir importar as notas do Teste de Progresso.                                |
| BS26 | A nota deve ser convertida para a escala de bônus definida pela instituição.                    |
| BS27 | A nota deve ser vinculada à disciplina escolhida pelo aluno.                                    |
| BS28 | Alunos ausentes não devem receber o bônus.                                                      |
| BS29 | O professor deve visualizar os alunos vinculados às suas disciplinas e respectivas notas.       |
| BS30 | O sistema deve manter registro das alterações realizadas nas notas.                             |
| BS31 | O sistema deve fornecer relatórios de adesão por curso, período e campus.                       |
| BS32 | O sistema deve fornecer informações sobre ocupação das salas.                                   |
| BS33 | O sistema deve permitir consultar dados consolidados de desempenho.                             |
| BS34 | O sistema deve restringir o acesso às informações de acordo com o perfil do usuário.            |
| BS35 | O sistema deve tratar os dados pessoais conforme os requisitos de proteção de dados aplicáveis. |
| BS36 | O sistema deve manter mecanismos de auditoria para alterações relevantes.                       |

## Conclusão

<p align="justify">
A terceira parte do brainstorm permitiu identificar os requisitos relacionados ao acompanhamento do Teste de Progresso após sua organização, incluindo registro de presença, lançamento das notas, disponibilização de informações aos diferentes usuários, proteção dos dados e geração de relatórios para apoio à gestão acadêmica.
</p>
