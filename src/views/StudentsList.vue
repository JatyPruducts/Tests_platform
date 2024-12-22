<template>
    <header>
        <b-navbar toggleable="lg" type="light" class="bg-info bg-gradient shadow">
            <div>
                <button type="button" class="btn border rounded p-2" data-bs-toggle="offcanvas" data-bs-target="#Sections" aria-controls="Sections" style="background-color: #f1faa3; color: black;">
                    <i class="bi bi-list"> Разделы</i>
                </button>
            </div>
                <b-nav-item-dropdown class="border rounded p-2" style="background-color: #f1faa3;font-size: large;" right>
                    <template #button-content>
                        <i class='bi bi-person-square'></i> 
                        <em> {{ name }}</em> <!--заменим на Имя из БД -->
                    </template>
                    <b-dropdown-item href="/teacher/profile/">Профиль</b-dropdown-item>
                    <b-dropdown-item href="#">Ученики</b-dropdown-item>
                </b-nav-item-dropdown>
        </b-navbar>
    </header>

    <body>
        <b-card>
            <b-card-body style="position:relative; height:87vh; overflow-y:scroll; text-align: left; font-size: large;">

            </b-card-body>
        </b-card>
    </body>
</template>

<script>
export default {
    name: 'StudentsList',
    }
</script>