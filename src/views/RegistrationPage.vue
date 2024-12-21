<template>  
    <div class="bg-white position-absolute mx-auto top-50 start-50 translate-middle 
    border border-opacity-25 p-3 shadow rounded" style="height: 770px; width: 400px;">
      <h2>Регистрация</h2>
      <b-form @submit="Registration" class="mx-auto border border-dark rounded border-opacity-25 p-3 shadow" style="height: 670px; width: 300px;">
        <b-form-group id="name" label="Имя:" label-for="input-4" class="text-start">
          <b-form-input id="input-4" type="text" placeholder="Введите имя" v-model="form.name"></b-form-input>
        </b-form-group>
        <b-form-group id="surname" label="Фамилия:" label-for="input-5" class="text-start">
          <b-form-input id="input-5" type="text" placeholder="Введите фамилию" v-model="form.surname"></b-form-input>
        </b-form-group>
        <b-form-group id="login" label="Логин:" label-for="input-1" class="text-start">
          <b-form-input id="input-1" type="text" placeholder="Введите логин" v-model="form.login"></b-form-input>
        </b-form-group>
        <b-form-group id="Role" label="Выберите роль:" label-for="input-4" class="text-start">
            <b-form-select v-model="selected" :options="roles"></b-form-select>
        </b-form-group>
        <b-form-group id="password" label="Пароль:" label-for="input-2" class="text-start">
          <b-form-input id="input-2" type="password" placeholder="Введите пароль" v-model="form.password"></b-form-input>
        </b-form-group>
        <b-form-group id="confirmPassword" label="Подтвердите пароль:" label-for="input-3" class="text-start">
          <b-form-input id="input-3" type="password" placeholder="Подтвердите пароль" v-model="form.confirmPassword"></b-form-input>
        </b-form-group>
        <h5>Имеется учетная запись?</h5>
        <b-link href="/">Войти</b-link> <br> <br>
        <b-button type="submit" variant="primary">Зарегистрироваться</b-button>
      </b-form>
    </div>
</template>
  
<script>
import axios from 'axios'
  export default {
    name: 'RegistrationPage',
    data(){
      return{
        form:{
          name:'',
          surname:'',
          login:'',
          password:'',
          confirmPassword:'',
          selected: "Student"
        },
        roles: [
            {value: "Student", text: 'Ученик'},
            {value: "Teacher", text: 'Учитель'}
        ]
      }
    },
    methods:
    {
        async Registration()
        {
          try{
            const response = await axios.post(`http://127.0.0.1:8000/users/`, {
            name: this.form.name,
            surname: this.form.surname,
            login: this.form.login,
            password: this.form.password,
            role: this.form.selected
            }); 
            // Логика при успешном входе
            alert('Добро пожаловать, ' + response.data.name +'!');
            this.$router.push('/admin/main'); 
          }
           catch(error){
            // Логика при ошибке входа
            alert('Ошибка входа: ' + error.response.data.detail);
          }
        } 
      }
    }
</script>