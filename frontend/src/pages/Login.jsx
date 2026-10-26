import { useState } from 'react'
import { Navigate, useLocation, useNavigate } from 'react-router-dom'
import { useAuth } from '../auth/AuthContext'
import { caminhoInicial } from '../components/menu'

// Tela 01 do protótipo · UC01
export default function Login() {
  const { usuario, entrar } = useAuth()
  const navigate = useNavigate()
  const location = useLocation()
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [erro, setErro] = useState('')
  const [enviando, setEnviando] = useState(false)

  if (usuario) return <Navigate to={caminhoInicial(usuario.perfil)} replace />

  async function handleSubmit(evento) {
    evento.preventDefault()
    setErro('')
    setEnviando(true)
    try {
      const dados = await entrar(username, password)
      const destino = location.state?.de?.pathname ?? caminhoInicial(dados.perfil)
      navigate(destino, { replace: true })
    } catch (e) {
      setErro(e.status === 401 ? 'Usuário ou senha inválidos.' : 'Não foi possível conectar à API.')
    } finally {
      setEnviando(false)
    }
  }

  return (
    <main className="login">
      <form onSubmit={handleSubmit} className="cartao">
        <h1>Teste de Progresso</h1>
        <p>Entre com sua credencial institucional.</p>
        <label>
          Usuário
          <input value={username} onChange={(e) => setUsername(e.target.value)} autoComplete="username" required />
        </label>
        <label>
          Senha
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            autoComplete="current-password"
            required
          />
        </label>
        {erro && <p role="alert" className="erro">{erro}</p>}
        <button type="submit" disabled={enviando}>
          {enviando ? 'Entrando…' : 'Entrar'}
        </button>
      </form>
    </main>
  )
}
