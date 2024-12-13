import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import ProfileAdmin from '../views/ProfileAdmin.vue';
import RegistrationPage from '@/views/RegistrationPage.vue';
const routes = [
    { path: '/', name:'home', component: HomePage },
    { path: '/admin/main/', name:'AdminProfile', component: ProfileAdmin},
    { path: '/registration', name:'registration', component: RegistrationPage }
];
const router = createRouter({
    history: createWebHistory(), 
    routes
  });
  
export default router;