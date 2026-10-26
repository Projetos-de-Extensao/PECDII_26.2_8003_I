import { useLocation } from 'react-router-dom'
import { useAuth } from '../auth/AuthContext'
import { MENU } from '../components/menu'

export default function EmConstrucao() {
  const { usuario } = useAuth()
  const { pathname } = useLocation()
  const item = (MENU[usuario.perfil] ?? []).find((i) => i.para === pathname)

  return (
    <section>
      <h1>{item?.rotulo ?? 'Página'}</h1>
      <p>Em construção{item?.sprint ? ` — prevista para a Sprint ${item.sprint}` : ''}.</p>
    </section>
  )
}
