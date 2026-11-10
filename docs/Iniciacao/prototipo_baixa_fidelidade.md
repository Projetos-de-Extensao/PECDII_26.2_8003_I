---
id: prototipo_baixa_fidelidade
title: Protótipo de Baixa Fidelidade
---

# Protótipo de Baixa Fidelidade — Teste de Progresso

## Introdução

<p align="justify">
O protótipo de baixa fidelidade representa, de forma simples e sem preocupação visual, as telas do Sistema do Teste de Progresso e o caminho que cada perfil percorre dentro dele. Seu objetivo é validar com o stakeholder (Pró-Reitoria Acadêmica) o fluxo das funcionalidades, os dados exibidos em cada tela e as regras de negócio levantadas no brainstorm, na pesquisa e nos casos de uso, antes da construção do protótipo de alta fidelidade.
</p>

## Metodologia

<p align="justify">
As telas foram derivadas dos casos de uso UC01 a UC15 e dos requisitos RF-01 a RF-34. Os wireframes foram desenhados com <b>PlantUML Salt</b>, que gera esboços em preto e branco a partir de texto e é renderizado diretamente na documentação pelo plugin PlantUML do MkDocs. Todos os nomes, matrículas e notas apresentados são fictícios, conforme o RNF-07.
</p>

## Mapa de navegação

```plantuml
@startuml
skinparam monochrome true
skinparam shadowing false
left to right direction

rectangle "01 Login" as T01

package "Aluno" {
  rectangle "02 Painel do aluno" as T02
  rectangle "03 Escolher turma" as T03
  rectangle "04 Atendimento especial" as T04
  rectangle "05 Revisão" as T05
  rectangle "06 Comprovante" as T06
  rectangle "07 Minha inscrição" as T07
  rectangle "08 Meus dados" as T08
}

package "Professor" {
  rectangle "09 Minha escala" as T09
  rectangle "10 Espelho de notas" as T10
}

package "Administração acadêmica" {
  rectangle "11 Gerenciar edição" as T11
  rectangle "12 Importar dados" as T12
  rectangle "13 Campi, salas e professores" as T13
  rectangle "14 Ensalamento e escala" as T14
  rectangle "15 Registrar presença" as T15
  rectangle "16 Processar notas" as T16
}

rectangle "17 Relatórios\n(Coordenação e Administração)" as T17

T01 --> T02 : aluno
T01 --> T09 : professor
T01 --> T11 : administração
T01 --> T17 : coordenação

T02 --> T03
T03 --> T04
T04 --> T05
T05 --> T06
T06 --> T07
T02 --> T07
T02 --> T08
T07 --> T03 : alterar turma

T09 --> T10

T11 --> T12
T12 --> T13
T13 --> T14
T14 --> T15
T15 --> T16
T16 --> T17
@enduml
```

## Versão 2.0

### Tela 01 — Login institucional

```plantuml
@startsalt
{+
  <b>Sistema do Teste de Progresso
  ==
  Usuário (credencial institucional)
  "matricula@instituicao.edu.br "
  Senha
  "****************            "
  [          Entrar          ]
  [ Entrar com conta institucional (SSO) ]
  ..
  Problemas de acesso? Procure o suporte de TI da instituição.
  Aviso de privacidade | Encarregado (DPO): dpo@instituicao.edu.br
}
@endsalt
```

- **UC01 · RF-01, RF-02.** Após autenticar, o usuário é direcionado ao painel do seu perfil (aluno, professor, coordenação ou administração).
- Não há "esqueci minha senha": a credencial é da instituição, então a recuperação é feita pelo suporte de TI.
- O aviso de privacidade e o contato do encarregado ficam visíveis desde o login (LGPD, art. 41).

### Tela 02 — Painel do aluno

```plantuml
@startsalt
{+
  {/ <b>Início | Minha inscrição | Meus dados | Sair }
  ==
  Olá, Ana Souza — Matrícula 2026000123 — Direito — 3º período — Campus Centro
  ..
  {+
    <b>Teste de Progresso 2026.2
    Inscrições: 01/09 a 30/09   |   Aplicação: 25/10, 14h
    Situação: <b>Inscrições abertas
    Sua inscrição: Não realizada
    [ Fazer inscrição ]
  }
  ..
  {+
    <b>Edições anteriores
    {#
      Edição | Situação | Bônus
      2026.1 | Presente | 0,72
      2025.2 | Ausente | —
    }
  }
}
@endsalt
```

- **UC04 · RF-09, RF-22.** Mostra a edição vigente, o prazo e o status da inscrição do aluno.
- Se já houver inscrição ativa, o botão muda para **Ver minha inscrição** (UC02, fluxo A2).
- Fora do período, o botão fica desabilitado e as datas são exibidas (UC02, A1).

### Tela 03 — Inscrição: escolher a turma do bônus

```plantuml
@startsalt
{+
  {/ Início | <b>Inscrição | Meus dados | Sair }
  ==
  <b>Inscrição — Teste de Progresso 2026.2
  Etapa 1 de 3: <b>Turma</b>  >  Atendimento especial  >  Revisão
  ..
  Escolha a turma que receberá o bônus (0 a 1).
  Só aparecem as turmas em que você está matriculado(a) neste semestre.
  {#
    . | Disciplina | Turma | Professor(a)
    () | Direito Civil III | DIR301-A | Prof. Carlos Lima
    (X) | Direito Penal II | DIR305-B | Profa. Marta Reis
    () | Processo Civil I | DIR310-A | Prof. João Alves
    () | Ética Profissional | DIR320-C | Profa. Lúcia Dias
  }
  ..
  [ Cancelar ] | [ Próximo > ]
}
@endsalt
```

- **UC02 · RF-10 · RN01, RN02, RN06.** Só é possível escolher uma turma, e ela precisa vir da matrícula vigente.
- A turma define a disciplina e o professor que receberão o espelho do bônus.
- Se não houver turma elegível, a lista é substituída pela orientação de procurar a secretaria (UC02, A3).

### Tela 04 — Inscrição: atendimento especial

```plantuml
@startsalt
{+
  {/ Início | <b>Inscrição | Meus dados | Sair }
  ==
  Etapa 2 de 3: Turma  >  <b>Atendimento especial</b>  >  Revisão
  ..
  Você precisa de atendimento especial para realizar a prova?
  () Não   | (X) Sim
  ..
  Tipo de atendimento
  ^Sala acessível (mobilidade reduzida)^
  Observações (opcional)
  "                                        "
  ..
  {+
    <b>Consentimento específico (dado sensível)
    Esta informação será usada somente para organizar sua sala de prova.
    O acesso é restrito à administração acadêmica, e o dado é excluído ao fim da edição.
    Você pode revogar este consentimento a qualquer momento.
    [X] Autorizo o tratamento desta informação para esta finalidade
  }
  ..
  [ < Voltar ] | [ Próximo > ]
}
@endsalt
```

- **UC02 (extensão "Solicitar atendimento especial") · RF-11 · RN04, RN05.**
- O campo é opcional. Quem responde **Não** não vê o bloco de consentimento.
- Se marcar **Sim** sem dar o consentimento, a inscrição não avança e o campo fica destacado (UC02, A5).

### Tela 05 — Inscrição: revisão e confirmação

```plantuml
@startsalt
{+
  {/ Início | <b>Inscrição | Meus dados | Sair }
  ==
  Etapa 3 de 3: Turma  >  Atendimento especial  >  <b>Revisão</b>
  ..
  {#
    Edição | Teste de Progresso 2026.2
    Data da prova | 25/10/2026, às 14h
    Campus | Centro
    Turma do bônus | Direito Penal II — DIR305-B
    Professor(a) | Profa. Marta Reis
    Atendimento especial | Sim — sala acessível
  }
  ..
  A turma pode ser alterada até 30/09, enquanto as inscrições estiverem abertas.
  ..
  [ < Voltar ] | [ Confirmar inscrição ]
}
@endsalt
```

- **UC02, passos 8 a 10.** No momento da confirmação, o sistema valida de novo o prazo e as regras.
- Se o prazo acabar durante o preenchimento, a inscrição não é confirmada (UC02, A6).

### Tela 06 — Comprovante de inscrição

```plantuml
@startsalt
{+
  {/ Início | <b>Inscrição | Meus dados | Sair }
  ==
  <b>Inscrição confirmada!
  ..
  {#
    Protocolo | TP-2026.2-000456
    Data | 15/09/2026, 10:32
    Aluno(a) | Ana Souza — 2026000123
    Turma do bônus | Direito Penal II — DIR305-B
    Campus | Centro
    Sala | A definir (será publicada até 18/10)
  }
  ..
  Enviamos a confirmação para ana.souza@instituicao.edu.br
  ..
  [ Baixar comprovante (PDF) ] | [ Ir para minha inscrição ]
}
@endsalt
```

- **UC02, passo 11 · RF-12, RF-14.**
- Se o e-mail falhar, o comprovante continua disponível aqui e o envio é tentado de novo (UC02, A7).

### Tela 07 — Minha inscrição (local e resultado)

```plantuml
@startsalt
{+
  {/ Início | <b>Minha inscrição | Meus dados | Sair }
  ==
  <b>Teste de Progresso 2026.2 — Protocolo TP-2026.2-000456
  ..
  {+
    <b>Inscrição
    Turma do bônus: Direito Penal II — DIR305-B (Profa. Marta Reis)
    Atendimento especial: Sim
    [ Alterar turma ] | [ Cancelar inscrição ]
    Disponível até 30/09
  }
  {+
    <b>Onde faço a prova
    Campus Centro — Bloco A — 2º andar — Sala A-204 (acessível)
    25/10/2026, às 14h. Chegue 30 minutos antes.
  }
  {+
    <b>Resultado
    Presença: Presente
    Bônus: <b>0,68</b> — lançado em Direito Penal II
  }
}
@endsalt
```

- **UC03, UC04 · RF-13, RF-22.** Os blocos aparecem conforme a etapa da edição:
    - "Onde faço a prova" só aparece depois que o ensalamento é publicado.
    - "Resultado" só aparece depois que as notas são publicadas.
- **Alterar** e **Cancelar** só ficam habilitados durante o período de inscrição (RN03).
- Pedido de realocação de sala: o aluno pode solicitar revisão da alocação automática (LGPD, art. 20).

### Tela 08 — Meus dados

```plantuml
@startsalt
{+
  {/ Início | Minha inscrição | <b>Meus dados | Sair }
  ==
  <b>O que o sistema guarda sobre você
  {#
    Dado | Finalidade | Compartilhado com
    Nome, matrícula, e-mail | Identificação e comunicação | Administração
    Curso, período, campus | Alocação de sala | Administração, coordenação
    Turma escolhida | Lançamento do bônus | Professor(a) da turma
    Presença e bônus | Registro acadêmico | Professor(a), sistema acadêmico
    Atendimento especial | Organizar sua sala | Somente administração
  }
  ..
  <b>Histórico de participação
  {#
    Edição | Turma | Presença | Bônus
    2026.1 | DIR201-A | Presente | 0,72
    2025.2 | DIR101-B | Ausente | —
  }
  ..
  [ Exportar CSV ] | [ Exportar PDF ] | [ Revogar consentimento ] | [ Solicitar correção ]
}
@endsalt
```

- **UC15 · RF-32 · LGPD, art. 18.** Garante acesso, portabilidade, revogação do consentimento (apenas para o atendimento especial) e pedido de correção.
- Os pedidos de correção são encaminhados ao encarregado (DPO) da instituição.

### Tela 09 — Professor: minha escala de aplicação

```plantuml
@startsalt
{+
  {/ <b>Minha escala | Espelho de notas | Sair }
  ==
  Profa. Marta Reis — Campus Centro
  ..
  <b>Teste de Progresso 2026.2 — 25/10/2026
  {#
    Horário | Local | Função | Alunos
    13h30 às 17h | Bloco A — Sala A-204 | Aplicadora titular | 38
  }
  ..
  <b>Documentos da sala
  [ Lista de presença (PDF) ] | [ Mapa de sala (PDF) ] | [ Etiqueta de porta (PDF) ]
  ..
  <b>Materiais que você receberá
  {#
    Cadernos de prova | 40
    Cartões-resposta | 40
    Envelopes lacrados | 2
  }
}
@endsalt
```

- **UC13 · RF-19, RF-20, RF-21.** O professor apenas consulta a escala; quem monta é a administração (Tela 14).
- As quantidades de material já incluem a margem de reserva.

### Tela 10 — Professor: espelho de notas

```plantuml
@startsalt
{+
  {/ Minha escala | <b>Espelho de notas | Sair }
  ==
  { Turma: | ^Direito Penal II — DIR305-B^ }
  Edição: Teste de Progresso 2026.2 — Resultados publicados em 10/11
  ..
  {#
    Matrícula | Aluno(a) | Presença | Bônus
    2026000123 | Ana Souza | Presente | 0,68
    2026000145 | Bruno Costa | Presente | 0,55
    2026000167 | Carla Nunes | Ausente | bloqueado
    2026000189 | Diego Rocha | Presente | 0,81
  }
  ..
  Alunos ausentes não recebem bônus.
  [ Exportar espelho (CSV) ]
}
@endsalt
```

- **UC12 · RF-26, RF-28 · RN15, RN17.** A tela é somente leitura: o professor não importa notas nem registra presença.
- Aparecem apenas as turmas sob responsabilidade do professor.

### Tela 11 — Administração: gerenciar edição

```plantuml
@startsalt
{+
  {/ <b>Edições | Dados | Salas | Ensalamento | Presença | Notas | Relatórios }
  ==
  <b>Nova edição
  {
    Nome | "Teste de Progresso 2026.2"
    Semestre | ^2026.2^
    Inscrições de | "01/09/2026" | até | "30/09/2026"
    Data da prova | "25/10/2026" | horário | "14:00"
  }
  ..
  <b>Campi participantes
  { [X] Centro | [X] Barra | [ ] Niterói }
  <b>Cursos participantes
  { [X] Direito | [X] Administração | [X] Economia | [ ] Engenharia }
  ..
  <b>Regra do bônus
  {
    Nota bruta mínima | "0" | máxima | "100"
    Bônus convertido de | "0" | até | "1"
    Turmas por aluno | "1"
    Margem de segurança das salas | "10 %"
  }
  ..
  [ Clonar edição anterior ] | [ Cancelar ] | [ Salvar edição ]
}
@endsalt
```

- **UC05 · RF-05, RF-06, RF-07, RF-08.** A faixa do bônus fica sempre entre 0 e 1 (RN14).
- Equilibrar a ocupação ou minimizar salas é uma configuração da edição, não uma regra fixa (Pesquisa, 2.7.2).

### Tela 12 — Administração: importar dados acadêmicos

```plantuml
@startsalt
{+
  {/ Edições | <b>Dados | Salas | Ensalamento | Presença | Notas | Relatórios }
  ==
  <b>Importar dados do sistema acadêmico — 2026.2
  {
    Tipo de arquivo: | ^Matrículas^ | .
    Arquivo CSV: | "matriculas_2026_2.csv" | [ Selecionar ]
  }
  [ Validar arquivo ]
  ..
  <b>Resultado da validação
  {#
    Arquivo | Linhas | Válidas | Com erro | Situação
    Alunos | 1.240 | 1.238 | 2 | Importado
    Turmas | 312 | 312 | 0 | Importado
    Matrículas | 6.870 | 6.861 | 9 | Pendente
    Professores | 145 | 145 | 0 | Importado
  }
  ..
  [ Baixar relatório de erros ] | [ Confirmar importação ]
}
@endsalt
```

- **UC06 · RF-03, RF-04.** A integração com o sistema acadêmico é feita por arquivo, não em tempo real.
- Linhas com erro ficam de fora até serem corrigidas.

### Tela 13 — Administração: campi, salas e professores

```plantuml
@startsalt
{+
  {/ Edições | Dados | <b>Salas | Ensalamento | Presença | Notas | Relatórios }
  ==
  { Campus: | ^Centro^ | [ + Nova sala ] }
  {#
    Sala | Bloco/andar | Cap. nominal | Cap. de prova | Acessível | Disponível
    A-101 | A / 1º | 60 | 40 | Sim | [X]
    A-204 | A / 2º | 50 | 38 | Sim | [X]
    B-110 | B / 1º | 45 | 30 | Não | [X]
    B-212 | B / 2º | 45 | 30 | Não | [ ]
  }
  ..
  <b>Professores disponíveis em 25/10
  {#
    Professor(a) | Campus de lotação | Turno | Disponível
    Marta Reis | Centro | Tarde | [X]
    Carlos Lima | Centro | Tarde | [X]
    João Alves | Barra | Tarde | [ ]
  }
  [ Salvar ]
}
@endsalt
```

- **UC07 · RF-15, RF-16 · RN07.** O ensalamento usa sempre a capacidade de prova, não a capacidade nominal.

### Tela 14 — Administração: ensalamento e escala

```plantuml
@startsalt
{+
  {/ Edições | Dados | Salas | <b>Ensalamento | Presença | Notas | Relatórios }
  ==
  { Edição 2026.2 — Campus: | ^Centro^ | Inscritos confirmados: 120 (3 com atendimento especial) }
  [ Gerar ensalamento automático ]
  ..
  <b>Proposta
  {#
    Sala | Cap. prova | Alunos | Ocupação | Aplicador(a) | Materiais
    A-101 (acessível) | 40 | 40 | 100% | Carlos Lima | 44
    A-204 (acessível) | 38 | 38 | 100% | Marta Reis | 42
    B-110 | 30 | 30 | 100% | <b>SEM APLICADOR | 33
    B-111 | 30 | 12 | 40% | Paulo Melo | 14
  }
  Reservas: Rita Gomes, Luiz Prado
  ..
  {+
    <b>Alertas
    Sala B-110 sem aplicador: escale um professor antes de publicar.
    Os 3 alunos com atendimento especial foram alocados em salas acessíveis.
  }
  ..
  [ Ajuste manual ] | [ Gerar documentos (PDF) ] | [ Publicar local de prova ]
}
@endsalt
```

Ajuste manual (abre ao clicar em **Ajuste manual**):

```plantuml
@startsalt
{+
  <b>Ajuste manual de alocação
  ==
  {
    Tipo: | ^Realocar aluno^
    Aluno(a): | ^2026000167 — Carla Nunes^
    Sala atual: | A-101
    Nova sala: | ^B-111^
  }
  Justificativa (obrigatória)
  "Solicitação de revisão aprovada pela coordenação"
  ..
  Será registrado na auditoria: autor, data, valor anterior e valor novo.
  [ Cancelar ] | [ Salvar ajuste ]
}
@endsalt
```

- **UC08, UC09 · RF-17 a RF-21, RF-23 · RN07 a RN13.**
- **Publicar** fica bloqueado enquanto houver uma violação de regra obrigatória: sala sem aplicador, falta de capacidade, falta de sala acessível ou inscrito sem sala (UC08, A1 a A4).
- Um ajuste manual que viole capacidade, campus ou acessibilidade é rejeitado, e a tela mostra a regra violada (UC08, A6).

### Tela 15 — Administração: registrar presença

```plantuml
@startsalt
{+
  {/ Edições | Dados | Salas | Ensalamento | <b>Presença | Notas | Relatórios }
  ==
  { Edição 2026.2 — Campus: | ^Centro^ | Sala: | ^A-204^ }
  ..
  {#
    Matrícula | Aluno(a) | Presente | Ausente
    2026000123 | Ana Souza | (X) | ()
    2026000145 | Bruno Costa | (X) | ()
    2026000167 | Carla Nunes | () | (X)
    2026000189 | Diego Rocha | (X) | ()
  }
  ..
  { Presentes: 36 | Ausentes: 2 }
  [ Importar lista digitalizada ] | [ Salvar presença ]
}
@endsalt
```

- **UC10 · RF-24.** A presença registrada aqui define quem pode receber o bônus (RN15).

### Tela 16 — Administração: processar notas e bônus

```plantuml
@startsalt
{+
  {/ Edições | Dados | Salas | Ensalamento | Presença | <b>Notas | Relatórios }
  ==
  { Edição 2026.2 — Arquivo de notas brutas: | "notas_2026_2.csv" | [ Selecionar ] | [ Processar ] }
  ..
  <b>Resumo do lote
  {#
    Processadas | Válidas | Bloqueadas (ausentes) | Inconsistentes
    1.180 | 1.152 | 21 | 7
  }
  ..
  <b>Inconsistências
  {#
    Matrícula | Problema | Ação
    2026000999 | Matrícula não encontrada | [ Excluir ]
    2026000412 | Nota fora da faixa (104) | [ Corrigir ]
    2026000533 | Turma sem professor responsável | [ Ver vínculo ]
  }
  ..
  [ Baixar inconsistências ] | [ Confirmar lote ] | [ Exportar CSV ao sistema acadêmico ] | [ Publicar resultados ]
}
@endsalt
```

- **UC11 · RF-25, RF-27, RF-28, RF-33 · RN14 a RN19.** Só registros válidos e confirmados são exportados.
- Um arquivo com estrutura inválida é rejeitado por inteiro (UC11, A1).
- Alterar uma nota já publicada exige justificativa e vai para a trilha de auditoria (UC11, A6).

### Tela 17 — Relatórios e indicadores

```plantuml
@startsalt
{+
  {/ Edições | Dados | Salas | Ensalamento | Presença | Notas | <b>Relatórios }
  ==
  { Edição: | ^2026.2^ | Curso: | ^Todos^ | Período: | ^Todos^ | Campus: | ^Todos^ | [ Filtrar ] }
  ..
  {/ <b>Adesão | Ocupação | Desempenho | Auditoria }
  {#
    Curso | Matriculados | Inscritos | Adesão | Presentes
    Direito | 820 | 610 | 74% | 588
    Administração | 540 | 350 | 65% | 331
    Economia | 310 | 220 | 71% | 214
  }
  ..
  [ Exportar CSV ] | [ Exportar PDF ]
}
@endsalt
```

- **UC14 · RF-29 a RF-31, RF-33, RF-34 · RN17.** A coordenação vê a mesma tela, mas restrita ao próprio curso e sem as abas administrativas.
- Os dados de desempenho são agregados e, sempre que possível, anonimizados.

## Versão 1.0

A primeira versão, em texto, tinha cinco telas: Login, Inscrição do Aluno, Painel do Professor, Ensalamento e Relatórios. A versão 2.0 fez estas mudanças:

- Cobre todos os casos de uso, de UC01 a UC15.
- Retira do professor a importação de notas e o registro de presença, que passam para a administração, como definido no UC10 e no UC11.
- Troca o "esqueci minha senha" pelo acesso institucional.
- Inclui atendimento especial com consentimento, comprovante e "Meus dados", para atender à LGPD.

## Rastreabilidade

| Tela | Caso de uso | Requisitos |
|---|---|---|
| 01 | UC01 | RF-01, RF-02 · BS01, BS02 |
| 02 | UC04 | RF-09, RF-22 |
| 03 | UC02 | RF-10 · BS06, BS07 |
| 04 | UC02 (extensão) | RF-11 |
| 05 | UC02 | RF-09 · BS05 |
| 06 | UC02 | RF-12, RF-14 · BS09 |
| 07 | UC03, UC04 | RF-13, RF-22 · BS08, BS23 |
| 08 | UC15 | RF-32 |
| 09 | UC13 | RF-19, RF-20, RF-21 |
| 10 | UC12 | RF-26, RF-28 · BS29 |
| 11 | UC05 | RF-05 a RF-08 · BS03, BS04 |
| 12 | UC06 | RF-03, RF-04 |
| 13 | UC07 | RF-15, RF-16 · BS10, BS11, BS17 |
| 14 | UC08, UC09 | RF-17 a RF-21, RF-23 · BS12 a BS22 |
| 15 | UC10 | RF-24 · BS24 |
| 16 | UC11 | RF-25, RF-27, RF-28, RF-33 · BS25 a BS28, BS30 |
| 17 | UC14 | RF-29 a RF-31, RF-34 · BS31 a BS33 |

## Conclusão

<p align="justify">
O protótipo de baixa fidelidade permitiu visualizar a jornada completa de cada perfil, do login à publicação do bônus, e confirmar que os casos de uso e as regras de negócio têm uma tela correspondente. Ele também deixou explícitas as premissas a validar com a Pró-Reitoria, como a diferença entre capacidade nominal e capacidade de prova e a escolha entre equilibrar a ocupação ou minimizar salas. Esse material servirá de base para o protótipo de alta fidelidade e para os diagramas de sequência.
</p>

## Referências

> PlantUML. Salt (wireframes). Disponível em: https://plantuml.com/salt

> Documentos do projeto: Pesquisa, Brainstorm e Casos de Uso do Teste de Progresso.

## Versionamento

| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| — | 1.0 | Protótipo textual com 5 telas | Equipe do projeto |
| 26/09/2026 | 2.0 | Wireframes em PlantUML Salt com 17 telas, mapa de navegação e rastreabilidade | Equipe do projeto |
