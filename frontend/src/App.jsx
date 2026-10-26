import { Navigate, Route, Routes } from 'react-router-dom'
import RotaProtegida from './auth/RotaProtegida'
import Layout from './components/Layout'
import EmConstrucao from './pages/EmConstrucao'
import Login from './pages/Login'
import Painel from './pages/Painel'

// Prefixo de rota de cada perfil. As páginas de cada sprint entram aqui.
const AREAS = {
  aluno: 'aluno',
  professor: 'professor',
  coordenacao: 'coordenacao',
  administracao: 'admin',
}

export default function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      {Object.entries(AREAS).map(([perfil, prefixo]) => (
        <Route
          key={perfil}
          path={`/${prefixo}`}
          element={
            <RotaProtegida perfis={[perfil]}>
              <Layout />
            </RotaProtegida>
          }
        >
          <Route index element={<Painel />} />
          <Route path="*" element={<EmConstrucao />} />
        </Route>
      ))}
      <Route path="*" element={<Navigate to="/login" replace />} />
    </Routes>
  )
}
