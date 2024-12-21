<template>  
    <div class="bg-white position-absolute mx-auto top-50 start-50 translate-middle 
    border border-opacity-25 p-3 shadow rounded" style="height: 700px; width: 400px;">
      <h2>Регистрация</h2>
      <b-form @submit="onSubmit" class="mx-auto border border-dark rounded border-opacity-25 p-3 shadow" style="height: 600px; width: 300px;">
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
        onSubmit(event)
        {
            event.preventDefault();
            //Проверка на пустые значения
            if (this.form.login == "") return document.getElementById("input-1").classList.add('is-invalid'); 
            document.getElementById("input-1").classList.remove('is-invalid');  
            if (this.form.password == "") return document.getElementById("input-2").classList.add('is-invalid');
            document.getElementById("input-2").classList.remove('is-invalid');
            if (this.form.confirmPassword == "") return document.getElementById("input-3").classList.add('is-invalid');
            document.getElementById("input-3").classList.remove('is-invalid');
            //Проверяем подтверждение пароля
            if (this.form.password != this.form.confirmPassword) 
            {
                this.form.confirmPassword = ""; 
                document.getElementById("input-3").placeholder = "Пароли не совпадают"
                return document.getElementById("input-3").classList.add('is-invalid');
            }
            document.getElementById("input-3").classList.remove('is-invalid');
        },
        async Registration()
        {
          const response = await axios.post(`http://127.0.0.1:8000/users/`, {
          user_login: this.form.login,
          user_password: this.form.password,
          user_role: this.form.selected
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
}
</script>