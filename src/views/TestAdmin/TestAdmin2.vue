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
        <b-card>
            <b-card-body v-if="!testCompleted" style="position:relative; height:80vh; overflow-y:scroll; text-align: left; font-size: large;">
                <h1>{{ testTitle }}</h1>
                <div v-html="text"></div>
            </b-card-body>
            
            <b-card-body v-else style="position:relative; height:80vh; overflow-y:auto; text-align: center;">
                <h1 class="mb-4">Тест завершен!</h1>
                <h3>Правильных ответов: {{ scorePercentage }}%</h3>
                <h3>Оценка: {{ grade }}</h3>
            </b-card-body>

            <b-card-footer v-if="!testCompleted">
                <b-button @click="checkAnswer" variant="success">Ответить</b-button>
                <b-button 
                    v-if="isAnswered" 
                    @click="nextTest" 
                    variant="primary"
                    class="ml-2"
                >
                    {{ isLastTest ? 'Завершить тест' : 'Следующий вопрос' }}
                </b-button>
            </b-card-footer>
        </b-card>
    </body>
</template>
  
  <script>
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
        nextTest() {
          if (this.isLastTest) {
              this.testCompleted = true;
          } else {
              const nextTest = this.tests[this.currentTestIndex + 1];
              this.loadTest(nextTest.title, nextTest.file);
          }
      },
        checkAnswer() {
          const selectedOption = document.querySelector('input[name="flexRadioDefault"]:checked');
          if (selectedOption) {
              const selectedId = selectedOption.id;
              const allOptions = document.querySelectorAll('.form-check-input');

              allOptions.forEach(option => {
                  if (option.id === this.correctAnswerId) {
                      option.parentElement.style.backgroundColor = 'lightgreen';
                  } else if (option.id === selectedId && selectedId !== this.correctAnswerId) {
                      option.parentElement.style.backgroundColor = 'lightcoral';
                  } else {
                      option.parentElement.style.backgroundColor = '';
                  }
              });

              this.correctAnswers[this.currentTestIndex] = (selectedId === this.correctAnswerId);
              this.isAnswered = true;
          }
      }
    }
  }
  </script>
  
  <style>
.active-test {
  font-weight: bold;
}
.form-check-label {
  display: block;
  padding: 8px;
  margin: 4px 0;
  border-radius: 4px;
  transition: background-color 0.3s;
}
  </style>
  