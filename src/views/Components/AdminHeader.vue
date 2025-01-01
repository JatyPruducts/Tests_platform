<template>
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
                <b-dropdown-item href="/admin/profile/">Профиль</b-dropdown-item>
                <b-dropdown-item href="/admin/manipulations/">Управление пользователями</b-dropdown-item>
            </b-nav-item-dropdown>
    </b-navbar>
</template>

<script>
    export default
    {
        name:"AdminHeader",
        data(){
            return {
                name: ""
            }
        },
        mounted() {
            const userData = localStorage.getItem('user');
            this.user = JSON.parse(userData);
            this.name = this.user.name;
        }
        
    }
</script>