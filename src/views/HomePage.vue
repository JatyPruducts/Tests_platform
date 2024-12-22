<template>  
  <div class="bg-white position-absolute mx-auto top-50 start-50 translate-middle 
  border border-opacity-25 p-3 shadow rounded" style="height: 420px; width: 400px;">
    <h2>Вход в аккаунт</h2>
    <b-form @submit="login" class="mx-auto border border-dark rounded border-opacity-25 p-3 shadow" style="height: 320px; width: 300px;">
      <b-form-group id="login" label="Логин:" label-for="input-1" class="text-start">
        <b-form-input id="input-1" type="text" placeholder="Введите логин" v-model="form.login"></b-form-input>
      </b-form-group>
      <b-form-group id="password" label="Пароль:" label-for="input-2" class="text-start">
        <b-form-input id="input-2" type="password" placeholder="Введите пароль" v-model="form.password"></b-form-input>
      </b-form-group>
      <h5>Нет учетной записи?</h5>
      <b-link href="/registration" style="font-size: large;">Зарегистрироваться</b-link> <br> <br>
      <b-button type="submit" variant="primary">Войти</b-button>
    </b-form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomePage',
  data(){
    return{
      form:{
        login:'',
        password:''
      }
    }
  },
  methods: {
    async login()
    {
      if (this.form.login == "") return document.getElementById("input-1").classList.add('is-invalid'); 
      document.getElementById("input-1").classList.remove('is-invalid');  
      if (this.form.password == "") return document.getElementById("input-2").classList.add('is-invalid');
      document.getElementById("input-2").classList.remove('is-invalid');
      try{
        const response = await axios.post(`http://127.0.0.1:8000/users/authorization/`, {
        login: this.form.login,
        password: this.form.password
      }); 
      // Логика при успешном входе
      console.log(response);
      localStorage.setItem('user', JSON.stringify(response.data));
      alert('Добро пожаловать, ' + response.data.name +'!');
      if (response.data.role == "Student")
            {
              this.$router.push('/student/main'); 
            }
            else if (response.data.role == "Teacher")
            {
              this.$router.push('/teacher/main'); 
            }
            else {this.$router.push('/admin/main');} 
     }
      catch (error) {
      if (error.response) {
        console.error(error.response.data); // Выводим всю информацию об ошибке
        alert('Ошибка входа: ' + error.response.data.detail);
      } else {
        alert('Ошибка при выполнении запроса: ' + error.response.data.detail);
        }
      }
    }
  }
};
</script>