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
      <b-link href="/registration">Зарегистрироваться</b-link> <br> <br>
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
    onSubmit(event)
    {
      var logex = "vanya"; //Пример логина, потом заменим на вводимое из БД
      var pasex = 123; //Пример пароля, потом заменим на вводимое из БД
      event.preventDefault();
      //Проверка на пустые значения
      if (this.form.login == "") return document.getElementById("input-1").classList.add('is-invalid'); 
      document.getElementById("input-1").classList.remove('is-invalid');  
      if (this.form.password == "") return document.getElementById("input-2").classList.add('is-invalid');
      document.getElementById("input-2").classList.remove('is-invalid');
      //Проверка на верно введенные значения
      if (this.form.login != logex) 
      {
        this.form.login = ""; 
        document.getElementById("input-1").placeholder = "Введите существующий логин"
        return document.getElementById("input-1").classList.add('is-invalid');
      }
      if (this.form.password != pasex) 
      {
        this.form.password = ""; 
        document.getElementById("input-2").placeholder = "Введите верный пароль"
        return document.getElementById("input-2").classList.add('is-invalid');
      }
      document.getElementById("input-1").classList.remove('is-invalid');
      document.getElementById("input-2").classList.remove('is-invalid');
      this.login();
      alert(JSON.stringify(this.form));
      //this.$router.push('/admin/main');
    },
    async login()
    {
        const response = await axios.get(`http://127.0.0.1:8000/users/{user_id}`, {
          user_login: this.form.login,
          user_password: this.form.password
        }); 
        if (response.data.success) {
            // Логика при успешном входе
            alert('Успешный вход!');
            this.$router.push('/admin/main'); 
        } else {
            // Логика при ошибке входа
            alert('Ошибка входа: ' + response.data.message);
      }
    }
  }
};
</script>