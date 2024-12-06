import { createApp } from 'vue'
import App from './App.vue'

import { BootstrapVue3 } from 'bootstrap-vue-3'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

import PortalVue from 'portal-vue';

const app = createApp(App);
app.use(BootstrapVue3)
app.use(PortalVue)

app.mount('#app')
