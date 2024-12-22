import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import LectionsAdmin from '../views/LectionsAdmin.vue';
import LectionsStudent from '../views/LectionsStudent.vue';
import LectionsTeacher from '../views/LectionsTeacher.vue';
import ProfileAdmin from '@/views/ProfileAdmin.vue';
import ProfileStudent from '@/views/ProfileStudent.vue';
import ProfileTeacher from '@/views/ProfileTeacher.vue';
import StudentsList from '@/views/StudentsList.vue';

import RegistrationPage from '@/views/RegistrationPage.vue';
const routes = [
    { path: '/', name:'home', component: HomePage },
    { path: '/admin/main/', name:'LectionsAdmin', component: LectionsAdmin},
    { path: '/registration', name:'registration', component: RegistrationPage },
    { path: '/student/main/', name:'LectionsStudent', component: LectionsStudent},
    { path: '/teacher/main/', name:'LectionsTeacher', component: LectionsTeacher},
    { path: '/teacher/profile/', name:'ProfileTeacher', component: ProfileTeacher},
    { path: '/student/profile/', name:'ProfileStudent', component: ProfileStudent},
    { path: '/admin/profile/', name:'ProfileAdmin', component: ProfileAdmin},
    { path: '/teacher/students/', name:'StudentsList', component: StudentsList}
];
const router = createRouter({
    history: createWebHistory(), 
    routes
  });
  
export default router;