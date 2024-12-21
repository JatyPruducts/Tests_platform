import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import ProfileAdmin from '../views/ProfileAdmin.vue';
import ProfileStudent from '../views/ProfileStudent.vue';
import ProfileTeacher from '../views/ProfileTeacher.vue';

import RegistrationPage from '@/views/RegistrationPage.vue';
const routes = [
    { path: '/', name:'home', component: HomePage },
    { path: '/admin/main/', name:'ProfileAdmin', component: ProfileAdmin},
    { path: '/registration', name:'registration', component: RegistrationPage },
    { path: '/student/main/', name:'ProfileStudent', component: ProfileStudent},
    { path: '/teacher/main/', name:'ProfileTeacher', component: ProfileTeacher},
];
const router = createRouter({
    history: createWebHistory(), 
    routes
  });
  
export default router;