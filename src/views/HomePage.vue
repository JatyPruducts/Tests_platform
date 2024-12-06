<template>  
  <div class="bg-white position-absolute mx-auto top-50 start-50 translate-middle 
  border border-opacity-25 p-3 shadow rounded" style="height: 50vb; width: 60vb;">
    <h2>Вход в аккаунт</h2>
    <b-form class="w-75 mx-auto border border-dark rounded border-opacity-25 p-3 shadow">
      <b-form-group id="login" label="Логин:" label-for="input-1" class="text-start" description="">
        <b-form-input id="input-1" type="text" placeholder="Введите логин"></b-form-input>
      </b-form-group>
      <b-form-group id="password" label="Пароль:" label-for="input-2" class="text-start" description="">
        <b-form-input id="input-2" type="password" placeholder="Введите пароль"></b-form-input>
      </b-form-group>
      <b-button variant="success">Войти</b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
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