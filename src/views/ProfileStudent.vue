<template>
    <b-navbar toggleable="lg" type="light" class="bg-info bg-gradient shadow">
        <div>
            <button type="button" class="btn border rounded p-2" data-bs-toggle="offcanvas" data-bs-target="#Sections" aria-controls="Sections" style="background-color: yellow; color: black;">
                <i class="bi bi-list"> Разделы</i>
            </button>
        </div>
            <b-nav-item-dropdown class="border rounded p-2" style="background-color: yellow;font-size: large;" right>
                <template #button-content>
                    <i class='bi bi-person-square'></i> 
                    <em> {{ Uname }}</em> <!--заменим на Имя из БД -->
                </template>
                <b-dropdown-item href="#">Профиль</b-dropdown-item>
            </b-nav-item-dropdown>
    </b-navbar>
</template>

<script>
export default {
    name: 'ProfileStudent'
    }
</script>