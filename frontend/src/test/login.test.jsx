import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter } from 'react-router-dom'
import { afterEach, describe, expect, it, vi } from 'vitest'
import App from '../App'
import { AuthProvider } from '../auth/AuthContext'

function respostaJson(status, corpo) {
  return Promise.resolve({ ok: status < 400, status, json: () => Promise.resolve(corpo) })
}

function renderizar(rota = '/login') {
  return render(
    <MemoryRouter initialEntries={[rota]} future={{ v7_startTransition: true, v7_relativeSplatPath: true }}>
      <AuthProvider>
        <App />
      </AuthProvider>
    </MemoryRouter>,
  )
}

async function fazerLogin() {
  await userEvent.type(screen.getByLabelText('Usuário'), 'aluno')
  await userEvent.type(screen.getByLabelText('Senha'), 'senha')
  await userEvent.click(screen.getByRole('button', { name: 'Entrar' }))
}

afterEach(() => vi.unstubAllGlobals())

describe('Login (UC01)', () => {
  it('leva o aluno ao painel com o menu do perfil', async () => {
    vi.stubGlobal('fetch', vi.fn((url) => {
      if (url.endsWith('/auth/token/')) return respostaJson(200, { access: 'a', refresh: 'r' })
      return respostaJson(200, { username: 'aluno', nome: 'Ana Souza', perfil: 'aluno', perfil_display: 'Aluno' })
    }))

    renderizar()
    await fazerLogin()

    expect(await screen.findByRole('heading', { name: 'Olá, Ana Souza' })).toBeInTheDocument()
    const menu = screen.getByRole('navigation', { name: 'Menu principal' })
    expect(menu).toHaveTextContent('Minha inscrição')
    expect(menu).not.toHaveTextContent('Ensalamento')
  })

  it('mostra erro quando a senha é inválida', async () => {
    vi.stubGlobal('fetch', vi.fn(() => respostaJson(401, { detail: 'No active account' })))

    renderizar()
    await fazerLogin()

    expect(await screen.findByRole('alert')).toHaveTextContent('Usuário ou senha inválidos.')
  })

  it('redireciona para o login quem não está autenticado', () => {
    renderizar('/admin')
    expect(screen.getByRole('button', { name: 'Entrar' })).toBeInTheDocument()
  })
})
