<template>
    <header>
        <div class="offcanvas offcanvas-start"  tabindex="-1" id="Sections" aria-labelledby="SectionsLabel" style="text-align: left;">
            <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="SectionsLabel">Оглавление</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
            </div>
            <div class="offcanvas-body">
                <ul>
                    <li v-for="lecture in lectures" :key="lecture.title">
                        <a href="#" @click.prevent="loadLecture(lecture.title, lecture.file)">{{ lecture.title }}</a>
                    </li>
                </ul>
            </div>
        </div>
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
                    <b-dropdown-item href="#">Статистика</b-dropdown-item>
                    <b-dropdown-item href="#">Учителя</b-dropdown-item>
                    <b-dropdown-item href="#">Ученики</b-dropdown-item>
                    <b-dropdown-item href="#">Пользователи</b-dropdown-item>
                </b-nav-item-dropdown>
        </b-navbar>
    </header>
    <body>
        <b-card>
            <b-card-body style="position:relative; height:85vh; overflow-y:scroll; text-align: left;">
                <h1>{{ lectureTitle }}</h1>
                <div v-html="text"></div>  <!--текст будем брать из текстового файла-->
            </b-card-body>
        </b-card>
    </body>
</template>

<script>
import mammoth from 'mammoth';

export default {
    name: 'ProfileAdmin',
    data() {
      return {
        Uname: "Иван",
        text: "",
        lectureTitle: "",
        lectures: [
            {title: "Лекция 1", file: "/lectures/SomeText.docx"},
            {title: "Лекция 2", file: "/lectures/Lecture2.docx"}
        ]
        };
    },
    methods: {
        async loadLecture(title, file) {
            this.lectureTitle = title; // Устанавливаем заголовок лекции из массива
            try {
                const response = await fetch(file);
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                const arrayBuffer = await response.arrayBuffer();
                const { value: html } = await mammoth.convertToHtml({ arrayBuffer });
                this.text = html; // Сохраняем HTML для отображения
            } catch (error) {
                console.error('Error fetching the lecture:', error);
            }
        }
    }
}
</script>