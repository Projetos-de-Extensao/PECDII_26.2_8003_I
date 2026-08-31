# Protótipo de Baixa Fidelidade — Teste de Progresso

## Tela 1 — Login
- Campo: **Usuário** (credencial institucional)
- Campo: **Senha**
- Botão: **Entrar**
- Link: **Esqueci minha senha**
- Observação: acesso por perfil (aluno, professor, coordenação, administração)

## Tela 2 — Inscrição do Aluno
- Cabeçalho: nome do aluno e edição do teste
- Lista: **disciplinas matriculadas** no semestre
- Seleção: **escolha da disciplina** que receberá a nota bônus (0 a 1)
- Botão: **Confirmar inscrição**
- Mensagem: confirmação e aviso do período de inscrição

## Tela 3 — Painel do Professor
- Lista: **disciplinas** do professor
- Lista: **alunos inscritos** por disciplina
- Coluna: **nota** (importada)
- Coluna: **presença** (presente/ausente)
- Botão: **Importar notas**
- Observação: ausentes não recebem bônus

## Tela 4 — Ensalamento (Coordenação/Administração)
- Lista: **campus e salas** com capacidade e acessibilidade
- Botão: **Gerar ensalamento automático**
- Lista: **distribuição dos alunos** por sala
- Lista: **escala de professores aplicadores** (1 por sala, sem duplicidade)
- Botão: **Ajuste manual** (com registro de quem alterou e por quê)
- Observação: cálculo de materiais por sala

## Tela 5 — Relatórios
- Filtros: **curso, período e campus**
- Relatório: **adesão** (quantos se inscreveram)
- Relatório: **ocupação das salas**
- Relatório: **desempenho consolidado**
- Botão: **Exportar**
- Observação: acesso restrito por perfil e auditoria de alterações