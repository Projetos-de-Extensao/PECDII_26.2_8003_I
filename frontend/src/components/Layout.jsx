import { NavLink, Outlet } from 'react-router-dom'
import { useAuth } from '../auth/AuthContext'
import { MENU } from './menu'

export default function Layout() {
  const { usuario, sair } = useAuth()
  const itens = MENU[usuario.perfil] ?? []

  return (
    <div className="layout">
      <header className="topo">
        <strong>Teste de Progresso</strong>
        <div className="topo-usuario">
          <span>
            {usuario.nome || usuario.username} · {usuario.perfil_display}
          </span>
          <button type="button" onClick={sair}>
            Sair
          </button>
        </div>
      </header>
      <nav className="menu" aria-label="Menu principal">
        {itens.map((item) => (
          <NavLink key={item.para} to={item.para} end>
            {item.rotulo}
          </NavLink>
        ))}
      </nav>
      <main className="conteudo">
        <Outlet />
      </main>
    </div>
  )
}
