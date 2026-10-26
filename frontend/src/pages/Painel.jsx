import { Link } from 'react-router-dom'
import { useAuth } from '../auth/AuthContext'
import { MENU } from '../components/menu'

// Painel inicial de cada perfil: atalhos para as funcionalidades do menu.
export default function Painel() {
  const { usuario } = useAuth()
  const atalhos = (MENU[usuario.perfil] ?? []).slice(1)

  return (
    <section>
      <h1>Olá, {usuario.nome || usuario.username}</h1>
      <p>Painel de {usuario.perfil_display.toLowerCase()}.</p>
      <ul className="atalhos">
        {atalhos.map((item) => (
          <li key={item.para}>
            <Link to={item.para}>{item.rotulo}</Link>
          </li>
        ))}
      </ul>
    </section>
  )
}
