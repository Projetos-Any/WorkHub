import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    // Se a porta estiver ocupada, falha com erro claro em vez de pular para
    // outra porta (o que quebraria o CORS da API).
    strictPort: true,
  },
})
