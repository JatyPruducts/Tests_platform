<template>
    <header>
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
    </header>
    <body>
        <b-card v-if="!testCompleted">
            <b-card-body style="position:relative; height:80vh; overflow-y:scroll; text-align: left; font-size: large;">
                <h1>{{ testTitle }}</h1>
                <div v-html="text"></div>
            </b-card-body>
            <b-card-footer>
                <b-button @click="checkAnswer" variant="success">Ответить</b-button>
                <b-button 
                    v-if="isAnswered" 
                    @click="nextTest" 
                    variant="primary"
                >
                    {{ isLastTest ? 'Завершить тест' : 'Следующий вопрос' }}
                </b-button>
            </b-card-footer>
        </b-card>
        
        <div v-else class="text-center mt-5">
            <h1>Тест завершен!</h1>
            <h3>Правильных ответов: {{ scorePercentage}}%</h3>
            <h3>Оценка: {{ grade }}</h3>
        </div>
    </body>
</template>
  
  <script>
  import axios from 'axios';
export default {
    name: 'TestAdmin2',
    data() {
        return {
            name: "",
            login: "",
            text: "",
            testTitle: "",
            currentTestIndex: 0,
            correctAnswerId: "true", // ID правильного ответа (Float)
            isAnswered: false, // Флаг, указывающий, был ли ответ дан
            testCompleted: false,
            tests: [
                { title: "Вопрос 1", file: "/tests/2/Вопрос 1.txt" },
                { title: "Вопрос 2", file: "/tests/2/Вопрос 2.txt" },
                { title: "Вопрос 3", file: "/tests/2/Вопрос 3.txt" },
                // Добавьте другие тесты здесь
            ],
            correctAnswers: [] // Массив для хранения результатов
        };
    },
    computed: {
        isLastTest() {
            return this.currentTestIndex === this.tests.length - 1;
        },
        scorePercentage() {
            if (this.correctAnswers.length === 0) return 0;
            const correctCount = this.correctAnswers.filter(Boolean).length;
            // Исправленная формула расчета
            return Math.round((correctCount / this.tests.length) * 100);
        },
        grade() {
            if (this.scorePercentage > 80) return 5;
            if (this.scorePercentage > 60) return 4;
            if (this.scorePercentage > 40) return 3;
            if (this.scorePercentage > 20) return 2;
            return 1;
        }
    },
    mounted() {
        const userData = localStorage.getItem('user');
        this.user = JSON.parse(userData);
        this.name = this.user.name;
        this.login = this.user.login;
        
        // Инициализируем массив результатов
        this.correctAnswers = new Array(this.tests.length).fill(false);
        // Загружаем первый тест при монтировании компонента
        if (this.tests.length > 0) {
            this.loadTest(this.tests[0].title, this.tests[0].file);
        }
    },
    methods: {
        async loadTest(title, file) {
            this.testTitle = title;
            this.currentTestIndex = this.tests.findIndex(test => test.title === title);
            this.isAnswered = false; // Сброс флага при загрузке нового теста
            try {
                const response = await fetch(file);
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                this.text = await response.text(); // Получаем текст файла
            } catch (error) {
                console.error('Error fetching the test:', error);
            }
        },
        async nextTest() {
            if (this.isLastTest) {
                try{
                const correctCount = this.correctAnswers.filter(Boolean).length;
                const result = Math.round((correctCount / this.tests.length) * 100);

                // Исправленный запрос с параметрами в query string
                await axios.post(
                    `http://127.0.0.1:8000/user/test-result`,
                    null, // Пустое тело запроса
                    {
                        params: { // Параметры в URL
                            user_login: this.login,
                            test_name: "Числовые типы данных",
                            result_data: result
                        }
                    }
                );
                this.testCompleted = true;
            }
            catch (error) {
                    if (error.response) {
                        // Обработка ошибок сервера
                        console.error('Ошибка сервера:', error.response.data);
                        console.error('Статус:', error.response.status);
                        console.error('Заголовки:', error.response.headers);
                    } else if (error.request) {
                        // Ошибки без ответа от сервера
                        console.error('Нет ответа от сервера:', error.request);
                    } else {
                        // Другие ошибки
                        console.error('Ошибка:', error.message);
                    }
                }
            } else {
                const nextTest = this.tests[this.currentTestIndex + 1];
                this.loadTest(nextTest.title, nextTest.file);
            }
        },
        checkAnswer() {
            const selectedOption = document.querySelector('input[name="flexRadioDefault"]:checked');
            if (selectedOption) {
                const selectedId = selectedOption.id;
                
                // Записываем результат ответа
                this.correctAnswers[this.currentTestIndex] = (selectedId === this.correctAnswerId);
                this.isAnswered = true;
            }
        },
    }
  }
  </script>
  
  <style>
  .active-test {
    font-weight: bold; /* Делает текст жирным */
  }
  </style>
  