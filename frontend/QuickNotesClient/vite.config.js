import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// Tailwindcss PLugin Import
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    tailwindcss(),
  ],
})
