import { createContext, useCallback, useContext, useEffect, useState } from 'react'
import { obterToken, obterUsuarioLogado } from '../api/auth'
import { tokens } from '../api/client'

const AuthContext = createContext(null)

export function AuthProvider({ children }) {
  const [usuario, setUsuario] = useState(null)
  const [carregando, setCarregando] = useState(Boolean(tokens.access))

  // Ao abrir o app com token salvo, recupera o usuário logado.
  useEffect(() => {
    if (!tokens.access) return
    obterUsuarioLogado()
      .then(setUsuario)
      .catch(() => tokens.limpar())
      .finally(() => setCarregando(false))
  }, [])

  const entrar = useCallback(async (username, password) => {
    tokens.salvar(await obterToken(username, password))
    const dados = await obterUsuarioLogado()
    setUsuario(dados)
    return dados
  }, [])

  const sair = useCallback(() => {
    tokens.limpar()
    setUsuario(null)
  }, [])

  return (
    <AuthContext.Provider value={{ usuario, carregando, entrar, sair }}>
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  return useContext(AuthContext)
}
