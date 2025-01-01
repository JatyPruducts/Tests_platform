<template>
    <header>
        <AdminHeader></AdminHeader>
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
import AdminHeader from './Components/AdminHeader.vue';

export default {
    name: 'ProfileAdmin',
    components:{
        AdminHeader
    },
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