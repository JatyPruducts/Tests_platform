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
                         
                        <em> {{ name }}</em> <!--заменим на Имя из БД -->
                    </template>
                    <b-dropdown-item href="/student/profile/">Профиль</b-dropdown-item>
                </b-nav-item-dropdown>
        </b-navbar>
    </header>
    <body>
        <b-card>
            <b-card-body style="position:relative; height:87vh; overflow-y:scroll; text-align: left; font-size: large;">
                <h3>Имя: {{ name }} <br></h3>
                <h3>Фамилия: {{ surname }} <br></h3>
                <h3>Роль: {{ role }} <br></h3>
                <h3>Логин вашего учителя: {{ teacherLogin }} <br> <br></h3>
                <b-button @click="LinkForm" variant="primary" id="LinkButton"> Присоединиться к учителю</b-button>
                <b-input-group prepend="Введите логин учителя:" class="mt-3 hidden" style="width: 50dvw;" id="LinkForm">
                    <b-form-input id="login"></b-form-input>
                    <b-button @click="LinkToTeacher" variant="success">Подключиться</b-button>
                </b-input-group>

                 <!-- Новая секция с результатами тестов -->
                <div class="mt-5">
                    <h3>Мои результаты тестов:</h3>
                    
                    <div v-if="testResults.length > 0">
                        <b-table :items="testResults" :fields="resultFields" striped hover>
                            <template #cell(test_name)="data">
                                {{ data.value }}
                            </template>
                            <template #cell(result)="data">
                                {{ data.value }}%
                            </template>
                            <template #cell(grade)="data">
                                {{ calculateGrade(data.value) }}
                            </template>
                        </b-table>
                    </div>

                    <div v-else class="empty-results">
                        <i class="bi bi-info-circle"></i>
                        Пока нет результатов тестов
                    </div>
                </div>
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
        teacherLogin:'отсутствует',
        testResults: [],
        resultFields: [
            { key: 'test_name', label: 'Название теста' },
            { key: 'result', label: 'Результат (%)' },
            { key: 'grade', label: 'Оценка' }
        ]
        }   
    },
    async mounted() 
    {
        const userData = localStorage.getItem('user');
        this.user = JSON.parse(userData);
        this.name = this.user.name;
        this.surname = this.user.surname;
        this.login = this.user.login;
        this.role = this.user.role;
        this.id = this.user.id;
        try{
            const response = await axios.get(`http://127.0.0.1:8000/students/${this.id}/`);
            if (response && response.data) 
            {
                document.getElementById("LinkButton").classList.add("hidden");
                this.teacherLogin = response.data.teacher_login;
            }
        } catch(error) {
            console.log(error.response.data.detail)
        }

        try {
            const resultsResponse = await axios.get(
                `http://127.0.0.1:8000/users/test_result/${this.login}`
            );
            
            const results = resultsResponse.data.result;
            this.testResults = Object.entries(results).map(([test_name, result]) => ({
                test_name,
                result,
                grade: result
            }));
        } catch(error) {
            console.error('Ошибка загрузки результатов:', error);
        }
        
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
        },
        calculateGrade(percentage) {
            if (percentage > 80) return 5;
            if (percentage > 60) return 4;
            if (percentage > 40) return 3;
            if (percentage > 20) return 2;
            return 1;
        },
    }
}
</script>
<style>
.hidden
{
    display: none;
}
.empty-results {
    background-color: rgba(241, 250, 163, 0.3);
    border: 2px solid rgb(241, 250, 163);
    border-radius: 8px;
    padding: 20px;
    margin-top: 15px;
    color: #4a4a4a;
    font-size: 1.1rem;
    display: flex;
    align-items: center;
    gap: 10px;
}
.bi-info-circle {
    font-size: 1.3rem;
    color: #6c757d;
}
</style>