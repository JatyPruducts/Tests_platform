<template>
    <header>
        <b-navbar toggleable="lg" type="light" class="bg-info bg-gradient shadow">
            <div>
                <b-button type="button" class="btn border rounded p-2" href="/student/main/" aria-controls="Sections" style="background-color: #f1faa3; color: black;">
                    <i class="bi bi-list"> Разделы</i>
                </b-button>
            </div>
                <b-nav-item-dropdown class="border rounded p-2" style="background-color: #f1faa3;font-size: large;" right>
                    <template #button-content>
                        <i class='bi bi-person-square'></i> 
                        <em> {{ name }}</em> <!--заменим на Имя из БД -->
                    </template>
                    <b-dropdown-item href="#">Профиль</b-dropdown-item>
                </b-nav-item-dropdown>
        </b-navbar>
    </header>
    <body>
        <b-card>
            <b-card-body style="position:relative; height:87vh; overflow-y:scroll; text-align: left; font-size: large;">
                Имя: {{ name }} <br>
                Фамилия: {{ surname }} <br>
                Роль: {{ role }} <br>
                Логин вашего учителя: {{ teacherLogin }} <br> <br>
                <b-button @click="LinkForm" variant="primary" id="LinkButton"> Присоединиться к учителю</b-button>
                <b-input-group prepend="Введите логин учителя:" class="mt-3 hidden" style="width: 50dvw;" id="LinkForm">
                    <b-form-input id="login"></b-form-input>
                    <b-button @click="LinkToTeacher" variant="success">Button</b-button>
                </b-input-group>
            </b-card-body>
        </b-card>
    </body>
</template>

<script>
import axios from 'axios'
export default {
    name: 'ProfileStudent',
    data() {
      return {
        name: "",
        surname:'',
        login:'',
        role:'',
        text: "",
        id:'',
        teacherLogin:'отсутствует'
        }   
    },
    mounted() 
    {
        const userData = localStorage.getItem('user');
        this.user = JSON.parse(userData);
        this.name = this.user.name;
        this.surname = this.user.surname;
        this.login = this.user.login;
        this.role = this.user.role;
        this.id = this.user.id;
        // if (this.teacherLogin)
        // {
        //     document.getElementById("LinkButton").classList.add("hidden");
        // }
    },
    methods:
    {
        LinkForm()
        {
            document.getElementById("LinkButton").classList.add("hidden");
            document.getElementById("LinkForm").classList.remove("hidden");
        },
        async LinkToTeacher()
        {
            const response = await axios.post(`http://127.0.0.1:8000/students/`, {
                user_id: this.id,
                teacher_login: document.getElementById("login").value,
            });
            this.teacherLogin = response.data.teacher_login;
            document.getElementById("LinkForm").classList.add("hidden");
        }
    }
}
</script>
<style>
.hidden
{
    display: none;
}
</style>