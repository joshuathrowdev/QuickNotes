import { createApp } from 'vue'

import App from './App.vue'

// Router Import
import router from './router/index.js'

// Styling Imports
import './styles/main.css'

createApp(App).use(router).mount('#app')
