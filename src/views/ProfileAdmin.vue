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
                    <b-dropdown-item href="#">Профиль</b-dropdown-item>
                    <b-dropdown-item href="#">Статистика</b-dropdown-item>
                    <b-dropdown-item href="#">Учителя</b-dropdown-item>
                    <b-dropdown-item href="#">Ученики</b-dropdown-item>
                    <b-dropdown-item href="#">Пользователи</b-dropdown-item>
                </b-nav-item-dropdown>
        </b-navbar>
    </header>
    <body>
        <b-card>
            <b-card-body style="position:relative; height:87vh; overflow-y:scroll; text-align: left; font-size: large;">
                Имя: {{ name }} <br>
                Фамилия: {{ surname }} <br>
                Роль: {{ role }} <br>
            </b-card-body>
        </b-card>
    </body>
</template>

<script>
export default {
    name: 'ProfileAdmin',
    data() {
      return {
        name: "",
        surname:'',
        login:'',
        role:'',
        text: "",
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
    }
}
</script>