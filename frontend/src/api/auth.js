import { api } from './client'

export const obterToken = (username, password) =>
  api('/auth/token/', { metodo: 'POST', corpo: { username, password }, autenticado: false })

export const obterUsuarioLogado = () => api('/auth/me/')
