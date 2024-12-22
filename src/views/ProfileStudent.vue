<template>
    <header>
        <div class="offcanvas offcanvas-start"  tabindex="-1" id="Sections" aria-labelledby="SectionsLabel" style="text-align: left;">
            <div class="offcanvas-header">
                <h3 class="offcanvas-title" id="SectionsLabel">Оглавление</h3>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
            </div>
            <div class="offcanvas-body border" style="font-size: large;">
                <ul>
                    <li v-for="lecture in lectures" :key="lecture.title">
                        <a href="#" 
                        @click.prevent="loadLecture(lecture.title, lecture.file)"
                        :class="{ 'active-lecture': lecture.title === lectureTitle }"
                        >
                        {{ lecture.title }}</a>
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
                    <b-dropdown-item href="#">Профиль</b-dropdown-item>
                </b-nav-item-dropdown>
        </b-navbar>
    </header>
    <body>
        <b-card>
            <b-card-body style="position:relative; height:80vh; overflow-y:scroll; text-align: left; font-size: large;">
                <h1>{{ lectureTitle }}</h1>
                <div v-html="text"></div>  <!--текст будем брать из текстового файла-->
            </b-card-body>
            <b-card-footer>
                <b-button @click="prevLecture" :disabled="currentLectureIndex === 0">Предыдущая лекция</b-button>
                <b-button @click="nextLecture" :disabled="currentLectureIndex === lectures.length - 1">Следующая лекция</b-button>
            </b-card-footer>
        </b-card>
    </body>
</template>

<script>
import mammoth from 'mammoth';

export default {
    name: 'ProfileStudent',
    data() {
      return {
        Uname: "",
        text: "",
        lectureTitle: "",
        currentLectureIndex: 0, // Индекс текущей лекции
        lectures: [
            {title: "Лекция 1", file: "/lectures/SomeText.docx"},
            {title: "Лекция 2", file: "/lectures/Lecture2.docx"}
        ]
        };
    },
    mounted() {
        // Загружаем первую лекцию при монтировании компонента
        if (this.lectures.length > 0) {
            this.loadLecture(this.lectures[0].title, this.lectures[0].file);
        }
        const userData = localStorage.getItem('user');
        this.user = JSON.parse(userData);
        this.Uname = this.user.name;
    },
    methods: {
        async loadLecture(title, file) {
            this.lectureTitle = title; // Устанавливаем заголовок лекции из массива
            this.currentLectureIndex = this.lectures.findIndex(lecture => lecture.title === title); 
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
        },
        prevLecture() {
            if (this.currentLectureIndex > 0) {
                const prevLecture = this.lectures[this.currentLectureIndex - 1];
                this.loadLecture(prevLecture.title, prevLecture.file);
            }
        },
        nextLecture() {
            if (this.currentLectureIndex < this.lectures.length - 1) {
                const nextLecture = this.lectures[this.currentLectureIndex + 1];
                this.loadLecture(nextLecture.title, nextLecture.file);
            }
        }
    }
}
</script>

<style>
.active-lecture {
    font-weight: bold; /* Делает текст жирным */
}
</style>