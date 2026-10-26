import { Navigate, useLocation } from 'react-router-dom'
import { useAuth } from './AuthContext'
import { caminhoInicial } from '../components/menu'

// Só renderiza a rota para usuários logados e, se informado, dos perfis permitidos.
export default function RotaProtegida({ perfis, children }) {
  const { usuario, carregando } = useAuth()
  const location = useLocation()

  if (carregando) return <p className="carregando">Carregando…</p>
  if (!usuario) return <Navigate to="/login" replace state={{ de: location }} />
  if (perfis && !perfis.includes(usuario.perfil)) {
    return <Navigate to={caminhoInicial(usuario.perfil)} replace />
  }
  return children
}
