import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import LectionsAdmin from '../views/LectionsAdmin.vue';
import LectionsStudent from '../views/LectionsStudent.vue';
import LectionsTeacher from '../views/LectionsTeacher.vue';
import ProfileAdmin from '@/views/ProfileAdmin.vue';
import ProfileStudent from '@/views/ProfileStudent.vue';
import ProfileTeacher from '@/views/ProfileTeacher.vue';
import StudentsList from '@/views/StudentsList.vue';
import TestTeacher1 from '@/views/TestTeacher/TestTeacher1.vue';
import TestTeacher2 from '@/views/TestTeacher/TestTeacher2.vue';
import TestTeacher3 from '@/views/TestTeacher/TestTeacher3.vue';
import TestAdmin1 from '@/views/TestAdmin/TestAdmin1.vue';
import TestAdmin2 from '@/views/TestAdmin/TestAdmin2.vue';
import TestAdmin3 from '@/views/TestAdmin/TestAdmin3.vue';
import TestStudent1 from '@/views/TestStudent/TestStudent1.vue';
import TestStudent2 from '@/views/TestStudent/TestStudent2.vue';
import TestStudent3 from '@/views/TestStudent/TestStudent3.vue';
import UserManipulation from '@/views/UserManipulation.vue';
import StudentDetails from '@/views/StudentDetails.vue';

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
    { path: '/teacher/students/', name:'StudentsList', component: StudentsList},
    { path: '/teacher/test/1/', name:'TestTeacher1', component: TestTeacher1},
    { path: '/teacher/test/2/', name:'TestTeacher2', component: TestTeacher2},
    { path: '/teacher/test/3/', name:'TestTeacher3', component: TestTeacher3},
    { path: '/admin/test/1/', name:'TestAdmin1', component: TestAdmin1},
    { path: '/admin/test/2/', name:'TestAdmin2', component: TestAdmin2},
    { path: '/admin/test/3/', name:'TestAdmin3', component: TestAdmin3},
    { path: '/student/test/1/', name:'TestStudent1', component: TestStudent1},
    { path: '/student/test/2/', name:'TestStudent2', component: TestStudent2},
    { path: '/student/test/3/', name:'TestStudent3', component: TestStudent3},
    { path: '/admin/manipulations/', name:'UserManipulation', component: UserManipulation},
    { path: '/student/:login/', name: 'StudentDetails', component: StudentDetails},

];
const router = createRouter({
    history: createWebHistory(), 
    routes
  });
  
export default router;