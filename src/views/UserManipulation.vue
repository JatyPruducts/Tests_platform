<template>
    <header>
        <b-navbar toggleable="lg" type="light" class="bg-info bg-gradient shadow">
            <div>
                <b-button type="button" class="btn border rounded p-2" href="/admin/main/" aria-controls="Sections" style="background-color: #f1faa3; color: black;">
                    <i class="bi bi-list"> Разделы</i>
                </b-button>
            </div>
                <b-nav-item-dropdown class="border rounded p-2" style="background-color: #f1faa3;font-size: large;" right>
                    <template #button-content>
                        <em> {{ name }}</em> <!--заменим на Имя из БД -->
                    </template>
                    <b-dropdown-item href="/admin/profile/">Профиль</b-dropdown-item>
                    <b-dropdown-item href="#">Управление пользователями</b-dropdown-item>
                </b-nav-item-dropdown>
        </b-navbar>
    </header>
    <body>
        <b-card>
            <b-card-body style="position:relative; height:87vh; overflow-y:scroll; text-align: left; font-size: large;">
                <div class="w-50">
                    <h1 >Поля для работы с кнопками</h1><br>
                    id:<b-form-input type="number" class="w-50" v-model="Uid"></b-form-input>
                    Имя:<b-form-input type="text" class="w-50" v-model="Uname"></b-form-input>
                    Фамилия:<b-form-input type="text" class="w-50" v-model="Usurname"></b-form-input>
                    Логин:<b-form-input type="text" class="w-50" v-model="Ulogin"></b-form-input>
                    Роль:<b-form-input type="text" class="w-50" v-model="Urole"></b-form-input>
                    Пароль:<b-form-input type="text" class="w-50" v-model="Upassword"></b-form-input><br>
                    <h1 >Кнопки управления</h1><br>
                    <b-button @click="adduser" variant="success">Создать пользователя</b-button>
                    <b-button @click="gubl" variant="primary">Данные о пользователе по логину</b-button>
                    <b-button @click="gau" variant="primary">Вывести список пользователей</b-button>
                    <b-button @click="gubid" variant="primary">Данные о пользователе по id</b-button>
                    <b-button @click="du" variant="danger">Удалить пользователя по id</b-button><br><br>
                    <b-button @click="cul" variant="success">Создать связь ученика с учителем</b-button>
                    <b-button @click="gal" variant="primary">Вывести все связи учеников с учителями</b-button>
                    <b-button @click="glbid" variant="primary">Найти связь по id ученика</b-button>
                    <b-button @click="dlbid" variant="danger">Удалить связь ученика с учителем по id ученика</b-button><br><br>
                    <b-button @click="ctl" variant="success">Создать возможность учителю подключать учеников</b-button>
                    <b-button @click="gatl" variant="primary">Вывести список учителей</b-button>
                    <b-button @click="gtlbid" variant="primary">Найти учителя по id</b-button>
                    <b-button @click="dtlbid" variant="danger">Удалить возможность учителю подключать учеников (по id)</b-button><br><br>
                    <b-button @click="gals" variant="primary">Вывести список учеников, связанных с учителем по его логину</b-button>
                    <div>{{text}}</div>
                </div>
            </b-card-body>
        </b-card>
    </body>
</template>

<script>
import axios from 'axios';

export default {
    name: 'UserManipulation',
    data() {
        return {
            name:'',
            Uname: "",
            Usurname: '',
            Ulogin: '',
            Urole: '',
            Upassword: '',
            Uid: '',
            text: '',
        };
    },
    mounted() {
        const userData = localStorage.getItem('user');
        this.user = JSON.parse(userData);
        if (this.user && this.user.name) { // Проверка наличия имени
            this.name = this.user.name;
        }
    },
    methods: {
        async adduser() {
            try {
                const response = await axios.post(`http://127.0.0.1:8000/users/`, {
                    name: this.Uname,
                    surname: this.Usurname,
                    login: this.Ulogin,
                    password: this.Upassword,
                    role: this.Urole
                });
                this.text = response.data; // Предполагая, что сервер возвращает JSON-строку
            } catch (error) {
                console.error('Ошибка:', error.response);
                this.text = 'Не удалось выполнить команду. Проверьте проблему в консоли!';
            }
        },
        async gubl()
        {
            const response = await axios.get(`http://127.0.0.1:8000/users/info/${this.Ulogin}`, {
                    login: this.Ulogin
            });
                this.text = response.data;
            },
        
        async gau()
        {
            const response = await axios.get(`http://127.0.0.1:8000/users/`);
            this.text = response.data;
        },
        async gubid()
        {
            const response = await axios.get(`http://127.0.0.1:8000/users/${this.Uid}`,{
                user_id: this.Uid
            });
            this.text = response.data;
        },
        async du()
        {
            const response = await axios.delete(`http://127.0.0.1:8000/users/${this.Uid}`);
            this.text = response.data.detail;
        },
        async cul()
        {
            const response = await axios.post(`http://127.0.0.1:8000/students/`,{
                user_id: this.Uid,
                teacher_login: this.Ulogin
            });
            this.text = response.data;
        },
        async gal()
        {
            const response = await axios.get(`http://127.0.0.1:8000/students/`);
            this.text = response.data;
        },
        async glbid()
        {
            const response = await axios.get(`http://127.0.0.1:8000/students/${this.Uid}`);
            this.text = response.data;
        },
        async dlbid()
        {
            const response = await axios.delete(`http://127.0.0.1:8000/students/${this.Uid}`);
            this.text = response.data.detail;
        },
        async ctl()
        {
            const response = await axios.post(`http://127.0.0.1:8000/teachers/`,{
                user_id: this.Uid,
                teacher_login: this.Ulogin
            });
            this.text = response.data;
        },
        async gatl()
        {
            const response = await axios.get(`http://127.0.0.1:8000/teachers/`);
            this.text = response.data;
        },
        async gtlbid()
        {
            const response = await axios.get(`http://127.0.0.1:8000/teachers/${this.Uid}`);
            this.text = response.data;
        },
        async dtlbid()
        {
            const response = await axios.delete(`http://127.0.0.1:8000/teachers/${this.Uid}`);
            this.text = response.data.detail;
        },
        async gals()
        {
            const response = await axios.get(`http://127.0.0.1:8000/students_by_teacher/${this.Ulogin}`);
            this.text = response.data;
        }
    }
}


</script>