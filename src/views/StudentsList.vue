<template>
    <header>
        <b-navbar toggleable="lg" type="light" class="bg-info bg-gradient shadow">
            <div>
                <b-button type="button" class="btn border rounded p-2" href="/teacher/main/" aria-controls="Sections" style="background-color: #f1faa3; color: black;">
                    <i class="bi bi-list"> Разделы</i>
                </b-button>
            </div>
                <b-nav-item-dropdown class="border rounded p-2" style="background-color: #f1faa3;font-size: large;" right >
                    <template #button-content>
                        <em> {{ name }}</em> <!--заменим на Имя из БД -->
                    </template>
                    <b-dropdown-item href="/teacher/profile/">Профиль</b-dropdown-item>
                    <b-dropdown-item href="#">Ученики</b-dropdown-item>
                </b-nav-item-dropdown>
        </b-navbar>
    </header>

    <body>
        <b-card>
            <b-card-body style="position:relative; height:87vh; overflow-y:scroll; text-align: left; font-size: large;">
                <h1>Ваши ученики:</h1>
                <b-table :items="students" :fields="fields" striped hover>
                <template #cell(name)="data">
                    <strong>{{ data.item.name }}</strong>
                </template>
                <template #cell(surname)="data">
                    <strong>{{ data.item.surname }}</strong>
                </template>
                <template #cell(login)="data">
                    <strong>{{ data.item.login }}</strong>
                </template>
                </b-table>
            </b-card-body>
        </b-card>
    </body>
</template>

<script>
import axios
 from 'axios';
export default {
    name: 'StudentsList',
    data() {
      return {
        name: "",
        login: '',
        students: [], // Здесь будут храниться данные о студентах
        fields: [
            { key: 'name', label: 'Имя' },
            { key: 'surname', label: 'Фамилия' },
            { key: 'login', label: 'Логин' },
        ],
        };
      },
    async mounted()
    {
        try {
        const userData = localStorage.getItem('user');
        this.user = JSON.parse(userData);
        this.name = this.user.name;
        this.login = this.user.login;
        const response = await axios.get(`http://127.0.0.1:8000/students_by_teacher/${this.login}`, {
            teacher_login: this.login
            }); 
        this.students = response.data;
    } catch(error)
    {
        alert('Ошибка: ' + error.response.data.detail);
    }
    },
}
</script>