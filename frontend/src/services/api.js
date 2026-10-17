// Único lugar do front que sabe onde a API está.
// As páginas chamam as funções daqui em vez de usar fetch direto.
const API_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000'

async function request(path, options = {}) {
  const response = await fetch(`${API_URL}${path}`, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  })

  if (!response.ok) {
    throw new Error(`Erro ${response.status} ao chamar ${path}`)
  }

  return response.json()
}

export function getHealth() {
  return request('/health')
}
