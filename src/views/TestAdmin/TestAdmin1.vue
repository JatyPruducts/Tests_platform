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
          <b-card-body style="position:relative; height:80vh; overflow-y:scroll; text-align: left; font-size: large;">
              <h1>{{ testTitle }}</h1>
              <div v-html="text"></div>
          </b-card-body>
          <b-card-footer>
              <b-button @click="checkAnswer" variant="success">Ответить</b-button>
              <b-button v-if="isAnswered" @click="nextTest" :disabled="currentTestIndex === tests.length - 1" variant="primary">Следующий вопрос</b-button>
          </b-card-footer>
      </b-card>
  </body>
</template>

<script>
export default {
  name: 'TestAdmin1',
  data() {
      return {
          name: "",
          text: "",
          testTitle: "",
          currentTestIndex: 0,
          correctAnswerId: "true", // ID правильного ответа (Float)
          isAnswered: false, // Флаг, указывающий, был ли ответ дан
          tests: [
              { title: "Вопрос 1", file: "/tests/1/Вопрос 1.txt" },
              { title: "Вопрос 2", file: "/tests/1/Вопрос 2.txt" },
              { title: "Вопрос 3", file: "/tests/1/Вопрос 3.txt" },
              { title: "Вопрос 4", file: "/tests/1/Вопрос 4.txt" },
              // Добавьте другие тесты здесь
          ]
      };
  },
  mounted() {
      const userData = localStorage.getItem('user');
      this.user = JSON.parse(userData);
      this.name = this.user.name;

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
          if (this.currentTestIndex < this.tests.length - 1) {
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
                      option.parentElement.style.backgroundColor = 'lightgreen'; // Правильный ответ
                  } else {
                      option.parentElement.style.backgroundColor = 'lightcoral'; // Неправильный ответ
                  }
              });

              if (selectedId !== this.correctAnswerId) {
                  selectedOption.parentElement.style.backgroundColor = 'lightcoral'; // Подсветка неправильного ответа
              }

              this.isAnswered = true; // Устанавливаем флаг после ответа
          }
      }
  }
}
</script>

<style>
.active-test {
  font-weight: bold; /* Делает текст жирным */
}
</style>
