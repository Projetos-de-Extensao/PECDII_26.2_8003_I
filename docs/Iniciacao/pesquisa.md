---
id: pesquisa
title: Pesquisa
---

# Pesquisa — Teste de Progresso

## 1. Capa

- **Tema:** Teste de Progresso — sistema de inscrição, alocação e lançamento de nota
- **Data:** 2026.2
- **Stakeholder:** Pró-Reitoria Acadêmica

---

## 2. Pesquisa

### 2.1 Contexto do Projeto

O Teste de Progresso é uma avaliação aplicada periodicamente a todos os alunos de um curso, independentemente do período em que estejam matriculados. Diferente de uma prova de disciplina, ele não mede um conteúdo isolado: mede o quanto o conhecimento do aluno evoluiu ao longo da graduação. O resultado serve tanto para o aluno se autoavaliar quanto para a instituição enxergar lacunas de formação e ajustar o projeto pedagógico do curso.

Hoje a operação do Teste de Progresso é conduzida de forma manual e fragmentada, com planilhas e comunicação por e-mail. Isso gera três dores concretas:

**a) Inscrição e vínculo da nota.** O aluno precisa se inscrever no teste e indicar em qual disciplina do semestre corrente a nota obtida será lançada como bônus (escala de 0 a 1). Sem um sistema, esse vínculo aluno → disciplina → professor é montado à mão, o que abre espaço para erro de lançamento, nota lançada em turma errada e retrabalho da secretaria acadêmica.

**b) Alocação física da aplicação.** A prova é presencial e simultânea. É preciso distribuir centenas de inscritos entre as salas disponíveis respeitando a capacidade de cada uma. A regra levantada em reunião parte de um exemplo prático: um curso com 120 inscritos, dividido em 3 salas, resulta em 40 alunos por sala. Esse cálculo hoje é feito manualmente para cada curso e cada campus.

**c) Escala de professores.** É necessário listar os docentes disponíveis, alocá-los como aplicadores/fiscais nas salas e cruzar essa escala com a listagem de disciplinas e a quantidade de alunos por disciplina. Sem consolidação, sobra sala sem fiscal e sobra professor sem alocação.

O projeto nasce dessa dor operacional: transformar um processo semestral, manual e sujeito a falhas em um fluxo digital com regras claras.

### 2.2 Objetivo

**Objetivo geral:** desenvolver uma solução digital que gerencie o ciclo completo do Teste de Progresso, da inscrição do aluno ao lançamento da nota bônus na disciplina escolhida, incluindo a alocação de salas, campus e professores aplicadores.

**Objetivos específicos:**

1. Permitir que o aluno se inscreva no Teste de Progresso dentro de um período definido pela Pró-Reitoria.
2. Permitir que o aluno escolha, no ato da inscrição, a disciplina em que a nota (0 a 1) será lançada, restrita às disciplinas em que ele está efetivamente matriculado no semestre.
3. Manter o cadastro e o relacionamento entre professores, disciplinas e turmas, para que o lançamento chegue ao docente correto.
4. Calcular a distribuição de inscritos por sala a partir da capacidade cadastrada de cada sala e do campus de aplicação.
5. Gerar a listagem de professores alocados por sala e a relação de alunos por disciplina.
6. Emitir relatórios gerenciais para a Pró-Reitoria Acadêmica: total de inscritos por curso, ocupação das salas, desempenho consolidado e notas a lançar por professor.

**Indicadores de sucesso propostos:** redução do tempo de preparação da logística de aplicação; eliminação de lançamentos manuais em planilha; percentual de inscritos alocados automaticamente sem intervenção; ausência de divergência entre a nota do teste e a nota lançada na disciplina.

### 2.3 Público-Alvo

| Ator | Papel no sistema | O que ganha |
|---|---|---|
| **Aluno** | Inscreve-se, escolhe a disciplina de destino da nota, consulta local de prova e resultado | Bônus de 0 a 1 na disciplina de sua escolha e autoavaliação do próprio progresso |
| **Professor** | Consulta a listagem de alunos que escolheram sua disciplina; atua como aplicador quando escalado | Recebe a nota já consolidada, sem conferência manual |
| **Coordenação de Curso** | Acompanha adesão e desempenho da sua turma | Diagnóstico de lacunas de formação por período |
| **Pró-Reitoria Acadêmica (stakeholder principal)** | Abre o período de inscrição, define regras, gera a logística e extrai relatórios | Processo auditável e insumo para avaliação institucional |
| **Secretaria Acadêmica / Apoio** | Cadastra salas, campus, capacidade e escala | Fim do controle por planilha |

### 2.4 Escopo

**Dentro do escopo (Parte I — Inscrição e Nota):**

- Cadastro e autenticação de alunos, professores e administradores.
- Abertura e fechamento do período de inscrição.
- Inscrição do aluno no Teste de Progresso.
- Seleção da disciplina de destino da nota, limitada às disciplinas em que o aluno está matriculado.
- Registro da nota no intervalo de 0 a 1 e vínculo com disciplina e professor responsável.
- Cadastro e manutenção do relacionamento professores × disciplinas × turmas.

**Dentro do escopo (Parte II — Logística de Aplicação):**

- Cadastro de campus e salas com respectiva capacidade.
- Distribuição automática dos inscritos por sala, respeitando a capacidade e o campus.
- Listagem de professores para alocação como aplicadores.
- Relatório de disciplinas com a quantidade de alunos vinculados.
- Emissão de mapa de sala e lista de presença.

**Fora do escopo (nesta entrega):**

- Elaboração, banco e revisão das questões da prova.
- Aplicação da prova em ambiente online e correção automática do gabarito — nesta versão a prova é presencial e a nota é importada/registrada.
- Integração em tempo real com o sistema acadêmico oficial da instituição (prevista via importação e exportação de arquivos).
- Módulo financeiro ou de emissão de certificados.
- Aplicativo mobile nativo.

**Premissas a validar com o stakeholder:**

- A regra "120 ÷ 3 = 40" representa a divisão de inscritos pela quantidade de salas disponíveis, e não um limite fixo de 40 alunos por sala.
- A nota bônus de 0 a 1 é somada à média final da disciplina escolhida, e não substitui avaliação existente.
- O aluno pode escolher apenas uma disciplina por edição do teste.
- Cada aluno realiza a prova no campus em que está matriculado.

### 2.5 Análise de Aplicações e Mercado

**Como o instrumento é usado hoje no Brasil.** O Teste de Progresso é um exame aplicado com regularidade, geralmente composto por questões de múltipla escolha, cuja finalidade é avaliar a evolução do estudante de forma progressiva e linear ao longo do curso. Ele funciona como instrumento de controle de qualidade das atividades de ensino-aprendizagem do currículo e, pelas aplicações sucessivas, permite verificar o progresso na aquisição de conhecimento tanto no plano individual quanto no das coortes. A prática é mais madura na área de saúde: na Medicina, o teste é aplicado anualmente sob coordenação da Associação Brasileira de Educação Médica (Abem), organizado em consórcios regionais que permitem comparação entre instituições. Já existem adaptações do modelo para outros cursos, como Fisioterapia, o que mostra que a expansão do instrumento para fora da saúde é um caminho consolidado.

**Soluções existentes e lacunas:**

| Categoria | Exemplos | O que resolve | O que não resolve |
|---|---|---|---|
| Plataformas comerciais de Teste de Progresso | Fornecedores especializados que ofertam banco de questões, aplicação e BI educacional para IES | Aplicação e análise de desempenho | Custo por aluno, dependência de fornecedor externo e pouca aderência a regras internas (ex.: bônus de 0 a 1 na disciplina) |
| Ambientes virtuais de aprendizagem | Moodle, Canvas, Google Forms | Aplicação de questionários e correção objetiva | Não tratam logística física: sala, campus, capacidade e escala de fiscais |
| Sistemas acadêmicos ERP | TOTVS RM, Lyceum, Jacad | Matrícula, diário e lançamento de nota | Não possuem módulo de Teste de Progresso nem alocação específica do evento |
| Softwares de alocação/timetabling | UniTime, FET | Distribuição de turmas em salas | Genéricos, sem vínculo com inscrição, nota bônus e relação professor × disciplina |

**Conclusão da análise.** O mercado cobre bem as pontas isoladas — aplicar prova, guardar nota, alocar sala — mas não há solução acessível que amarre as três em um fluxo único com a regra de negócio específica da instituição: inscrição voluntária, escolha da disciplina de destino da nota e distribuição por campus. É exatamente nessa lacuna que o projeto se posiciona, com a vantagem de ser desenvolvido sob medida para as regras da Pró-Reitoria Acadêmica e sem custo de licenciamento por aluno.

### 2.6 Funcionalidades

Prioridade em MoSCoW: M obrigatória, S desejável, C opcional.

Módulo 1 — Acesso e Cadastro Base
Código	Funcionalidade	Prior.
RF-01	Autenticação com credencial institucional, com SSO quando disponível	M
RF-02	Perfis de acesso: aluno, professor, coordenação, administração (RBAC)	M
RF-03	Importação de alunos, disciplinas, turmas e matrículas via CSV do sistema acadêmico	M
RF-04	Cadastro manual de exceções (aluno em situação especial, disciplina não importada)	S
Módulo 2 — Edição do Teste
Código	Funcionalidade	Prior.
RF-05	Criar edição do teste: semestre, data, horário, campi e cursos participantes	M
RF-06	Abrir e fechar o período de inscrição por data	M
RF-07	Configurar a regra do bônus (faixa 0 a 1 e limite de disciplinas por aluno)	M
RF-08	Clonar configuração de uma edição anterior	C
Módulo 3 — Inscrição (Parte I)
Código	Funcionalidade	Prior.
RF-09	Aluno realiza inscrição na edição aberta	M
RF-10	Seleção da disciplina de destino da nota, listando apenas as disciplinas em que está matriculado no semestre	M
RF-11	Solicitação de atendimento especial, com consentimento específico e destacado	M
RF-12	Emissão de comprovante de inscrição	S
RF-13	Cancelamento ou troca de disciplina até o fechamento do período	S
RF-14	Notificação por e-mail de confirmação e de local de prova	S
Módulo 4 — Alocação de Recursos (Parte II)
Código	Funcionalidade	Prior.
RF-15	CRUD de campus e salas com capacidade nominal, capacidade de prova e acessibilidade	M
RF-16	Cadastro de professores com campus de lotação e disponibilidade na data	M
RF-17	Geração automática do ensalamento respeitando capacidade e campus	M
RF-18	Ajuste manual da alocação, com registro de quem alterou e por quê	M
RF-19	Escala automática de aplicadores por sala, com fiscal reserva	M
RF-20	Cálculo de material por sala: cadernos, cartões-resposta, listas e envelopes, com margem de reserva	S
RF-21	Emissão de mapa de sala, lista de presença e etiqueta de porta em PDF	M
RF-22	Consulta "onde faço prova" pelo aluno	M
RF-23	Alerta de capacidade insuficiente antes do fechamento das inscrições	S
Módulo 5 — Notas
Código	Funcionalidade	Prior.
RF-24	Registro de presença e ausência por sala	M
RF-25	Importação da nota bruta e conversão para a escala de 0 a 1	M
RF-26	Espelho por professor com os alunos que escolheram sua disciplina e a nota a lançar	M
RF-27	Exportação das notas em CSV para o sistema acadêmico	M
RF-28	Bloqueio de lançamento para aluno ausente	M
Módulo 6 — Relatórios e Autoatendimento
Código	Funcionalidade	Prior.
RF-29	Adesão por curso, período e campus	M
RF-30	Taxa de ocupação das salas e resumo da escala	S
RF-31	Desempenho médio por curso e período, em dados agregados	S
RF-32	Tela "Meus dados" do aluno, com exportação do próprio histórico	M
RF-33	Trilha de auditoria de toda criação e alteração de nota	M
RF-34	Comparativo longitudinal entre edições (evolução da coorte)	C
Requisitos não funcionais
Código	Requisito
RNF-01	Aplicação web responsiva, utilizável em celular no dia da prova
RNF-02	Conformidade com a LGPD, conforme detalhado em 2.9.2
RNF-03	Suportar pico de acessos no primeiro e no último dia de inscrição
RNF-04	Gerar o ensalamento de uma edição completa em tempo aceitável para uso interativo
RNF-05	Trilha de auditoria imutável e backup com teste periódico de restauração
RNF-06	Acessibilidade seguindo WCAG 2.1 nível AA
RNF-07	Ambientes de teste e homologação com dados mascarados ou sintéticos

### 2.7 Alocação de Recursos

Esta é a parte mais complexa do sistema e corresponde à Parte II do levantamento. O problema é: distribuir N inscritos em M salas de capacidades diferentes, garantindo fiscalização e material suficientes, respeitando restrições de campus e acessibilidade.

#### 2.7.1 Recursos gerenciados
Recurso	Atributos relevantes	Papel na alocação
Sala	Código, campus, bloco, andar, capacidade nominal, capacidade de prova, acessível (sim/não), possui projetor/relógio	Container com capacidade limitada
Professor	Matrícula, campus de lotação, disponibilidade na data e turno, papel (aplicador, reserva, coordenador de andar)	Recurso escasso vinculado 1:N a salas
Aluno	Matrícula, curso, período, campus, disciplina escolhida, necessidade de atendimento especial	Item a ser distribuído
Recurso material	Caderno de prova, cartão-resposta, lista de presença, envelope/lacre, canetas	Consumível calculado a partir da alocação
Campus	Endereço, salas disponíveis na data	Fronteira rígida da alocação

#### 2.7.2 Restrições

Rígidas — a alocação é inválida se violadas:

Total de alunos em uma sala ≤ capacidade de prova da sala.
Aluno alocado apenas em sala do campus em que está matriculado.
Toda sala ocupada tem ao menos um aplicador designado.
Um professor não pode ser escalado em duas salas no mesmo horário.
Aluno com atendimento especial deferido vai para sala acessível.
Nenhum inscrito confirmado fica sem sala.

Flexíveis — buscam-se, mas admitem violação:

Equilibrar a ocupação entre as salas em vez de lotar uma e esvaziar outra. É exatamente a regra do quadro: com 120 inscritos e 3 salas, o resultado desejado é 40/40/40, não 50/50/20.
Misturar cursos e períodos na mesma sala, reduzindo colaboração indevida.
Minimizar o número de salas usadas, já que cada sala aberta consome um fiscal.
Escalar o professor no campus onde ele já leciona, reduzindo deslocamento.

Observe que 7 e 9 competem entre si: equilibrar tende a abrir mais salas, minimizar salas tende a lotar. A decisão precisa ser um parâmetro configurável pela Pró-Reitoria, não uma regra fixa no código.

#### 2.7.3 Lógica de alocação proposta

Heurística em quatro fases, sem necessidade de solver externo:

Apurar demanda. Agrupar inscritos confirmados por campus. Separar quem tem atendimento especial deferido.
Selecionar salas. Ordenar as salas do campus por capacidade de prova decrescente e selecionar até cobrir a demanda com folga de segurança (parâmetro, sugestão de 10%). Reservar antes as salas acessíveis para o grupo do passo 1.
Distribuir de forma balanceada. Calcular n_salas = teto(inscritos ÷ capacidade_média) e alvo_por_sala = teto(inscritos ÷ n_salas), preenchendo em round-robin e nunca ultrapassando a capacidade individual de cada sala. Intercalar alunos de cursos e períodos diferentes atende à restrição flexível 8.
Escalar aplicadores e material. Um aplicador por sala ocupada, mais reservas por andar; material calculado como alunos_na_sala + margem.

Capacidade nominal ≠ capacidade de prova. Uma sala de 50 lugares normalmente comporta bem menos alunos em situação de prova, por causa do espaçamento entre carteiras. O sistema deve guardar os dois números e usar sempre o segundo na alocação — isso não estava explícito no levantamento e precisa ser confirmado com a Pró-Reitoria.

#### 2.7.4 Cenários de teste da regra
Cenário	Entrada	Resultado esperado
Divisão exata (caso do quadro)	120 inscritos, 3 salas de 40	40 / 40 / 40 — ocupação de 100%
Divisão com resto	127 inscritos, 3 salas de 45	43 / 42 / 42 — diferença máxima de 1 aluno entre salas
Capacidade insuficiente	130 inscritos, 3 salas de 40	Bloquear a geração e alertar: faltam 10 vagas; sugerir abrir 4ª sala
Sala heterogênea	100 inscritos; salas de 60, 30 e 20	Respeitar o teto individual: 60 / 30 / 10, sem forçar média
Atendimento especial	3 alunos com deferimento	Alocados em sala acessível antes da distribuição geral
Fiscal insuficiente	4 salas ocupadas, 3 professores disponíveis	Alertar a lacuna antes da publicação da escala

#### 2.7.5 Entidades previstas (insumo para a fase de Elaboração)

Campus 1:N Sala · Edicao 1:N Inscricao · Aluno 1:N Inscricao · Inscricao 1:1 Disciplina escolhida · Professor N:M Disciplina · Alocacao (inscricao, sala, edicao, ordem/carteira) · EscalaAplicacao (professor, sala, edicao, papel) · RecursoMaterial N:M Sala por edição, com quantidade.

O par Alocacao e EscalaAplicacao são entidades associativas com atributo próprio — vale destacá-las no diagrama de classes.

### 2.8 Análise de Aplicações e Mercado

#### 2.8.1 Como o instrumento funciona hoje no Brasil

O Teste de Progresso é um exame aplicado com regularidade, geralmente de múltipla escolha, com a finalidade de acompanhar a evolução do estudante de maneira progressiva ao longo do curso. Funciona como instrumento de controle de qualidade do currículo e, pelas aplicações sucessivas, permite verificar o progresso na aquisição de conhecimento tanto no plano individual quanto no das coortes. A prática é mais madura na saúde: na Medicina o teste é aplicado anualmente sob coordenação da Associação Brasileira de Educação Médica (Abem), em consórcios regionais que permitem comparação entre instituições. Existem também consórcios interinstitucionais em São Paulo que aplicam o teste a cursos como Enfermagem, Farmácia, Fisioterapia, Nutrição, Odontologia, Psicologia e Educação Física, e adaptações do modelo já publicadas para Fisioterapia — sinal de que levar o instrumento para fora da saúde é caminho consolidado.

#### 2.8.2 Aplicações similares
Aplicação	O que faz	O que aproveitar	Limitação para o nosso caso
Plataforma A (Grupo A / SAGAH)	Avaliações para IES com banco de questões alinhado a ENADE e DCNs, TRI e ensalamento da instituição	É a referência mais próxima da Parte II: prova o valor do ensalamento integrado à avaliação	Suíte comercial ampla, licenciada por aluno, sem a regra do bônus na disciplina escolhida
Fábrica de Provas	Banco com centenas de milhares de questões, correção automática, recursos antifraude e registro auditável de cada ação	O conceito de trilha auditável ponta a ponta é diretamente reaproveitável no nosso RF-33	Foco no ciclo da prova, não na logística de recursos
Educat	Banco de questões com histórico de uso, calibração de itens e análise por Teoria Clássica dos Testes	Mostra o que a Pró-Reitoria vai querer na fase de relatórios: dificuldade e discriminação por item	Cobre a análise, não a inscrição nem a alocação
QuestCore	Montagem de avaliações, aplicação online e presencial, correção automatizada e integrações com LMS/ERP	Padrão de integração com ERP acadêmico, tema do nosso RF-03 e RF-27	Solução de fábrica de software, com custo e dependência de fornecedor
Minha Prova	Criação, aplicação e correção com leitura óptica de cartões-resposta, geração de versões A/B/C/D e acompanhamento longitudinal	Leitura óptica de cartão é o caminho natural para alimentar o RF-25 sem digitação	Voltada principalmente à educação básica
Moodle / Google Forms	Aplicação de questionários e correção objetiva	Custo zero e já presentes na instituição	Não tratam sala, campus, capacidade, fiscal nem material
UniTime / FET (open source)	Alocação de turmas e horários em salas	Algoritmos de alocação com restrições rígidas e flexíveis, base conceitual da seção 2.7	Genéricos, sem vínculo com inscrição e nota bônus
ERPs acadêmicos (TOTVS, Lyceum, Jacad)	Matrícula, diário de classe e lançamento de nota	Fonte de dados via importação	Não possuem módulo de Teste de Progresso

#### 2.8.3 Matriz comparativa de funcionalidades
Funcionalidade	Plataformas de avaliação	LMS	Timetabling	ERP acadêmico	Nosso projeto
Inscrição voluntária na edição	Parcial	Parcial	Não	Não	Sim
Escolha da disciplina de destino da nota	Não	Não	Não	Não	Sim
Bônus de 0 a 1 na média	Não	Não	Não	Parcial	Sim
Ensalamento por capacidade e campus	Parcial	Não	Sim	Não	Sim
Escala de professores aplicadores	Não	Não	Parcial	Não	Sim
Dimensionamento de material	Não	Não	Não	Não	Sim
Banco de questões e correção	Sim	Sim	Não	Não	Fora de escopo
Análise de item (TRI/TCT)	Sim	Parcial	Não	Não	Fora de escopo

#### 2.8.4 Conclusão da análise

O mercado resolve bem as pontas isoladas — elaborar e corrigir prova, guardar nota, alocar sala — e a Plataforma A chega perto ao juntar avaliação com ensalamento. Nenhuma das soluções pesquisadas, porém, cobre a regra de negócio específica levantada com o stakeholder: inscrição voluntária com escolha da disciplina que receberá um bônus de 0 a 1, combinada com alocação de salas, fiscais e material por campus. É nessa lacuna que o projeto se posiciona, com a vantagem de ser sob medida e sem custo de licenciamento por aluno. A decisão consciente é não competir em banco de questões e análise psicométrica, onde os fornecedores já são fortes, e sim integrar-se a eles por importação de notas.

### 2.9 Levantamento de Legislação

#### 2.9.1 Visão geral das normas aplicáveis

| Norma | O que exige | Onde impacta o sistema |
|---|---|---|
| **Lei nº 13.709/2018 (LGPD)** | Regras para todo tratamento de dados pessoais | Todo o sistema — detalhado em 2.9.2 |
| **Resolução CD/ANPD nº 15/2024** | Procedimento de comunicação de incidente de segurança | Plano de resposta a incidentes e registro de logs |
| **Lei nº 10.861/2004 (SINAES)** | Institui a avaliação das instituições, dos cursos e do desempenho dos estudantes | Resultados agregados alimentam a autoavaliação da CPA; exige rastreabilidade dos dados |
| **Lei nº 9.394/1996 (LDB), art. 47 e 53** | Autonomia da IES para fixar critérios de avaliação e aproveitamento | Fundamenta a regra do bônus de 0 a 1, desde que prevista em regulamento interno |
| **Decreto nº 9.235/2017, art. 104** | Determina a guarda do acervo acadêmico | Nota lançada em disciplina compõe registro acadêmico |
| **Portaria MEC nº 315/2018 e nº 360/2022** | Obrigam o acervo acadêmico digital, com confiabilidade, autenticidade, integridade e durabilidade; vedam emissão de documentos físicos para o acervo a partir de 1º/08/2022 | Registro da nota precisa ser nato-digital, íntegro e auditável |
| **Lei nº 13.146/2015 (LBI), art. 30** | Atendimento diferenciado em processos seletivos e avaliativos | Campo de solicitação de condições especiais e priorização de salas acessíveis |
| **Lei nº 12.965/2014 (Marco Civil), art. 15** | Guarda de registros de acesso a aplicações por 6 meses | Política de logs do sistema |
| **Regulamento interno / Resolução do Colegiado** | Institui o Teste de Progresso na IES | Fonte formal das regras de negócio — documento a solicitar ao stakeholder |

#### 2.9.2 LGPD aplicada ao projeto

**a) Papéis definidos (art. 5º, VI a VIII).** A IES é a **controladora** dos dados, pois define as finalidades e os meios do tratamento. A equipe de desenvolvimento e eventuais serviços de hospedagem atuam como **operadores**, tratando dados em nome da controladora. A IES já deve possuir um **encarregado (DPO)**, cujo contato precisa aparecer no aviso de privacidade da tela de inscrição (art. 41, § 1º).

**b) Inventário dos dados tratados (base para o registro do art. 37).**

| Dado | Categoria | Finalidade no sistema | Base legal |
|---|---|---|---|
| Nome, matrícula, e-mail institucional | Pessoal comum | Identificar o inscrito e comunicar local de prova | Art. 7º, V — execução de contrato educacional |
| Curso, período, campus | Pessoal comum | Alocar sala e agrupar resultados por coorte | Art. 7º, V |
| Disciplina escolhida e professor vinculado | Pessoal comum | Direcionar o lançamento da nota bônus | Art. 7º, V |
| Nota obtida (0 a 1) e presença | Pessoal comum | Compor avaliação e registro acadêmico | Art. 7º, II — cumprimento de obrigação legal/regulatória (Decreto 9.235/2017; Portaria 315/2018) |
| Solicitação de atendimento especial (deficiência, condição de saúde) | **Sensível** (art. 5º, II) | Garantir acessibilidade na aplicação | Art. 11, I — consentimento específico e destacado, com apoio no art. 11, II, "a" (obrigação legal da LBI) |
| Resultados agregados por curso e período | Anonimizado, quando possível | Avaliação institucional e CPA | Art. 12 c/c art. 7º, II |
| Logs de acesso (IP, data/hora, ação) | Pessoal comum | Auditoria e segurança | Art. 7º, II (Marco Civil, art. 15) e art. 7º, IX |

**c) Por que não usar consentimento como base geral.** O consentimento (art. 7º, I) é revogável a qualquer momento (art. 8º, § 5º) e é frágil em relações assimétricas, como a de aluno e instituição. Se o consentimento fosse a base do lançamento de nota, a revogação obrigaria a apagar um registro acadêmico obrigatório, o que é inviável. Por isso, o desenho adota execução de contrato e obrigação legal como bases principais, reservando o consentimento apenas para o dado sensível de atendimento especial, onde ele é exigido de forma específica e destacada.

**d) Princípios do art. 6º convertidos em decisões de projeto.**

| Princípio | Decisão no sistema |
|---|---|
| Finalidade e adequação (I, II) | O aviso de privacidade descreve exatamente as três finalidades: inscrição, alocação e lançamento de nota. Nenhum uso secundário sem nova análise |
| **Necessidade (III)** | Não coletar CPF, telefone, endereço, RG ou foto — a matrícula institucional é suficiente para identificar o aluno. Este é o ponto de maior risco em sistemas acadêmicos: coletar "por garantia" |
| Livre acesso e transparência (IV, VI) | Tela "Meus dados" mostrando o que o sistema guarda sobre o aluno e com quem compartilha |
| Qualidade dos dados (V) | Disciplinas ofertadas ao aluno vêm da matrícula vigente, evitando escolha de turma inexistente |
| Segurança e prevenção (VII, VIII) | Ver item (g) |
| **Não discriminação (IX)** | A nota do teste não pode ser usada para restringir matrícula, bolsa ou acesso a atividades. É bônus, nunca penalidade |
| Responsabilização (X) | Log imutável de quem lançou, alterou ou consultou nota |

**e) Alunos menores de 18 anos (art. 14).** Calouros com 17 anos são comuns. O tratamento de dados de adolescentes deve ocorrer em seu melhor interesse, e o art. 14, § 3º veda condicionar a participação em atividade a fornecimento de dados além do estritamente necessário. Requisito derivado: o formulário de inscrição não pode ter campos opcionais obrigatórios disfarçados, e o cadastro precisa marcar a data de nascimento apenas para essa verificação de regime.

**f) Direitos do titular (art. 18) como requisitos funcionais.**

| Direito | Requisito de sistema |
|---|---|
| Confirmação e acesso (I, II) | Tela de autoconsulta do aluno |
| Correção (III) | Fluxo de solicitação de correção de disciplina escolhida antes do fechamento das inscrições |
| Anonimização, bloqueio ou eliminação de dado desnecessário (IV) | Rotina de expurgo de dados operacionais após o encerramento da edição |
| Portabilidade (V) | Exportação do próprio histórico de participação em CSV ou PDF |
| Informação sobre compartilhamento (VII) | Listar no aviso de privacidade: coordenação, docente da disciplina escolhida e CPA |
| Revogação do consentimento (IX) | Aplicável apenas ao atendimento especial, com efeito imediato |

O art. 19, § 1º, II fixa **prazo de 15 dias** para resposta completa ao titular — a solicitação deve ser roteada ao encarregado da IES, não tratada pela equipe do projeto.

**g) Segurança da informação (arts. 46 a 49).**

- Controle de acesso por perfil (RBAC): aluno vê só os próprios dados; professor vê apenas os alunos que escolheram sua disciplina; coordenação vê o próprio curso; Pró-Reitoria vê o consolidado.
- Senhas armazenadas com hash e salt (bcrypt ou argon2), nunca em texto puro.
- Tráfego exclusivamente sobre HTTPS/TLS.
- Trilha de auditoria com data, hora, usuário e valor anterior em toda alteração de nota.
- **Ambientes de teste e homologação com dados mascarados ou sintéticos.** Popular banco de desenvolvimento com base real de alunos é tratamento sem base legal e é uma falha recorrente em projetos acadêmicos.
- Backup com retenção definida e teste periódico de restauração.

**h) Incidentes de segurança (art. 48 e Resolução CD/ANPD nº 15/2024).** A comunicação à ANPD e ao titular deve ocorrer em **três dias úteis**, contados do momento em que o controlador toma conhecimento de que o incidente afetou dados pessoais; para agentes de tratamento de pequeno porte o prazo é contado em dobro. A comunicação pode ser complementada em até vinte dias úteis, e o registro do incidente deve ser mantido por no mínimo cinco anos, mesmo quando não houver comunicação. Requisito derivado: o sistema precisa de log suficiente para responder o que vazou, de quantos titulares e quando — sem isso, a IES não consegue cumprir o prazo.

**i) Decisão automatizada (art. 20).** A alocação automática de sala e campus é uma decisão tomada por algoritmo que afeta o interesse do aluno. Deve existir canal de solicitação de revisão e realocação manual, com registro do motivo.

**j) Retenção e eliminação (arts. 15 e 16).**

| Dado | Prazo proposto | Justificativa |
|---|---|---|
| Nota lançada em disciplina | Permanente, no acervo acadêmico digital | Compõe registro acadêmico (Decreto 9.235/2017; Portarias 315/2018 e 360/2022) |
| Inscrição, alocação de sala e escala de professores | 2 edições (1 ano), depois anonimização | Dado operacional sem função probatória após a aplicação |
| Solicitação de atendimento especial | Até o fim da edição, salvo renovação pelo aluno | Dado sensível: minimizar exposição |
| Logs de acesso | 6 meses (Marco Civil, art. 15) | Guarda legal mínima |
| Resultados agregados/anonimizados | Indefinido | Anonimizados não são dados pessoais (art. 12) |

**k) Governança e sanções.** Recomenda-se, antes do desenvolvimento: (i) inclusão do sistema no **registro das operações de tratamento** da IES (art. 37); (ii) elaboração de **Relatório de Impacto à Proteção de Dados Pessoais — RIPD** (art. 38), justificada pelo volume de titulares e pela presença de dado sensível; (iii) contrato ou termo com cláusulas de proteção de dados com qualquer operador de hospedagem, incluindo verificação de transferência internacional (art. 33) se o servidor estiver fora do Brasil. O descumprimento sujeita a IES às sanções do art. 52, entre elas multa de até 2% do faturamento no Brasil, limitada a R$ 50 milhões por infração, além de bloqueio ou eliminação dos dados envolvidos.

#### 2.9.3 Pendências para a próxima etapa

1. Obter junto à Pró-Reitoria a resolução interna que institui o Teste de Progresso e define a regra do bônus de 0 a 1.
2. Obter o aviso de privacidade e a política de segurança da informação vigentes na IES, para herdar os textos em vez de criar novos.
3. Identificar o encarregado (DPO) da instituição e validar com ele as bases legais propostas em 2.9.2 (b).
4. Confirmar se o sistema será hospedado em infraestrutura própria da IES ou em nuvem de terceiro, o que muda a análise de operador e de transferência internacional.

---

## Referências

- BRASIL. Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais.
- BRASIL. Lei nº 10.861, de 14 de abril de 2004 — SINAES.
- BRASIL. Lei nº 9.394, de 20 de dezembro de 1996 — LDB.
- BRASIL. Lei nº 13.146, de 6 de julho de 2015 — Lei Brasileira de Inclusão.
- BRASIL. Lei nº 12.965, de 23 de abril de 2014 — Marco Civil da Internet.
- BRASIL. Decreto nº 9.235, de 15 de dezembro de 2017.
- ANPD. Resolução CD/ANPD nº 15, de 24 de abril de 2024 — Regulamento de Comunicação de Incidente de Segurança.
- MEC. Portaria nº 315, de 4 de abril de 2018; Portaria nº 332, de 13 de março de 2020; Portaria nº 360, de 18 de maio de 2022.
- PASCON, D. et al. Teste de progresso como instrumento de avaliação em saúde: uma revisão integrativa. Revista Meta: Avaliação, v. 14, n. 44, 2022.
- Reflexões sobre a utilização do Teste de Progresso na avaliação programática do estudante. Revista Brasileira de Educação Médica.
