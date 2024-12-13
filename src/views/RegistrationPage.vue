<template>  
    <div class="bg-white position-absolute mx-auto top-50 start-50 translate-middle 
    border border-opacity-25 p-3 shadow rounded" style="height: 530px; width: 400px;">
      <h2>Регистрация</h2>
      <b-form @submit="onSubmit" class="mx-auto border border-dark rounded border-opacity-25 p-3 shadow" style="height: 430px; width: 300px;">
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
  export default {
    name: 'RegistrationPage',
    data(){
      return{
        form:{
          login:'',
          password:'',
          confirmPassword:''
        },
        selected: "Schoolboy",
        roles: [
            {value: "Schoolboy", text: 'Ученик'},
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
        }
    }
}
</script>