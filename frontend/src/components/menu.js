// Itens de menu por perfil (RF-02). A API continua sendo quem garante o acesso.
export const MENU = {
  aluno: [
    { para: '/aluno', rotulo: 'Início' },
    { para: '/aluno/inscricao', rotulo: 'Minha inscrição', sprint: 2 },
    { para: '/aluno/meus-dados', rotulo: 'Meus dados', sprint: 5 },
  ],
  professor: [
    { para: '/professor', rotulo: 'Início' },
    { para: '/professor/escala', rotulo: 'Escala de aplicação', sprint: 3 },
    { para: '/professor/espelho', rotulo: 'Espelho de notas', sprint: 4 },
  ],
  coordenacao: [
    { para: '/coordenacao', rotulo: 'Início' },
    { para: '/coordenacao/indicadores', rotulo: 'Indicadores', sprint: 5 },
  ],
  administracao: [
    { para: '/admin', rotulo: 'Início' },
    { para: '/admin/edicoes', rotulo: 'Edições', sprint: 1 },
    { para: '/admin/importacoes', rotulo: 'Importações', sprint: 1 },
    { para: '/admin/salas', rotulo: 'Campi e salas', sprint: 1 },
    { para: '/admin/ensalamento', rotulo: 'Ensalamento', sprint: 3 },
    { para: '/admin/presenca', rotulo: 'Presença', sprint: 4 },
    { para: '/admin/notas', rotulo: 'Notas e bônus', sprint: 4 },
    { para: '/admin/indicadores', rotulo: 'Indicadores', sprint: 5 },
  ],
}

export function caminhoInicial(perfil) {
  return MENU[perfil]?.[0].para ?? '/login'
}
