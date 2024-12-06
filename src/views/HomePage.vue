<template>  
  <div class="bg-white position-absolute mx-auto top-50 start-50 translate-middle 
  border border-opacity-25 p-3 shadow rounded" style="height: 50vb; width: 60vb;">
    <h2>Вход в аккаунт</h2>
    <b-form @submit="onSubmit" class="w-75 mx-auto border border-dark rounded border-opacity-25 p-3 shadow">
      <b-form-group id="login" label="Логин:" label-for="input-1" class="text-start">
        <b-form-input id="input-1" type="text" placeholder="Введите логин" v-model="form.login"></b-form-input>
      </b-form-group>
      <b-form-group id="password" label="Пароль:" label-for="input-2" class="text-start">
        <b-form-input id="input-2" type="password" placeholder="Введите пароль" v-model="form.password"></b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Войти</b-button>
    </b-form>
  </div>
</template>

<script>
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
        document.getElementById("input-2").placeholder = "Введите существующий пароль"
        return document.getElementById("input-2").classList.add('is-invalid');
      }
      document.getElementById("input-1").classList.remove('is-invalid');
      document.getElementById("input-2").classList.remove('is-invalid');
      alert(JSON.stringify(this.form));
    }
  }
};
</script>

<style>
html, body
{
  height: 95%; 
  background: rgb(222,253,255 );
  background: linear-gradient(0deg, rgba(222,253,255,1) 0%, rgba(255,255,255,1) 50%, rgba(222,253,255,1) 100% );
}
</style>