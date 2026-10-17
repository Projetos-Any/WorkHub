import { useEffect, useState } from 'react'
import { getHealth } from '../services/api.js'

export default function Home() {
  const [apiStatus, setApiStatus] = useState('verificando...')

  useEffect(() => {
    getHealth()
      .then((data) => setApiStatus(data.status))
      .catch(() => setApiStatus('fora do ar'))
  }, [])

  return (
    <section className="card">
      <h1>Orçamentos em menos de 1 minuto</h1>
      <p>Crie e envie orçamentos profissionais direto do celular.</p>
      <p className={apiStatus === 'ok' ? 'status status--ok' : 'status'}>
        API: {apiStatus}
      </p>
    </section>
  )
}
