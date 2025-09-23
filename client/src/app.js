import './assets/main.css'

import { createApp } from 'vue'
import Home from './Home.vue'
import Upload from './Upload.vue'

createApp(Home).mount('#home')
createApp(Upload).mount('#upload')
