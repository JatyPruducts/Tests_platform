import { createApp } from 'vue';
import App from './App.vue';
import { BootstrapVue3 } from 'bootstrap-vue-3';

// Импортируйте CSS файлы
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-icons/font/bootstrap-icons.css';
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css';
import './style.css'
import router from './router'
import PortalVue from 'portal-vue';

const app = createApp(App);

app.use(BootstrapVue3);
app.use(PortalVue);
app.use(router);
app.mount('#app');