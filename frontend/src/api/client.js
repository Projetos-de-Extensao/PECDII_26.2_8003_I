// Cliente HTTP único: URL base, token JWT e tratamento de erros da API.
const API_URL = import.meta.env.VITE_API_URL ?? 'http://127.0.0.1:8000/api/v1'

const ACCESS_KEY = 'tp.access'
const REFRESH_KEY = 'tp.refresh'

export const tokens = {
  get access() {
    return localStorage.getItem(ACCESS_KEY)
  },
  get refresh() {
    return localStorage.getItem(REFRESH_KEY)
  },
  salvar({ access, refresh }) {
    if (access) localStorage.setItem(ACCESS_KEY, access)
    if (refresh) localStorage.setItem(REFRESH_KEY, refresh)
  },
  limpar() {
    localStorage.removeItem(ACCESS_KEY)
    localStorage.removeItem(REFRESH_KEY)
  },
}

export class ApiError extends Error {
  constructor(status, dados) {
    super(dados?.detail ?? `Erro ${status} na API`)
    this.status = status
    this.dados = dados
  }
}

async function enviar(caminho, { metodo = 'GET', corpo, autenticado = true } = {}) {
  const headers = { 'Content-Type': 'application/json' }
  if (autenticado && tokens.access) headers.Authorization = `Bearer ${tokens.access}`

  return fetch(`${API_URL}${caminho}`, {
    method: metodo,
    headers,
    body: corpo === undefined ? undefined : JSON.stringify(corpo),
  })
}

async function renovarToken() {
  if (!tokens.refresh) return false
  const resposta = await enviar('/auth/token/refresh/', {
    metodo: 'POST',
    corpo: { refresh: tokens.refresh },
    autenticado: false,
  })
  if (!resposta.ok) return false
  tokens.salvar(await resposta.json())
  return true
}

export async function api(caminho, opcoes = {}) {
  let resposta = await enviar(caminho, opcoes)

  // Access expirado: tenta renovar uma vez com o refresh token.
  if (resposta.status === 401 && opcoes.autenticado !== false && (await renovarToken())) {
    resposta = await enviar(caminho, opcoes)
  }

  const dados = resposta.status === 204 ? null : await resposta.json().catch(() => null)
  if (!resposta.ok) throw new ApiError(resposta.status, dados)
  return dados
}
