<template>
    <header>
      <b-navbar toggleable="lg" type="light" class="bg-info bg-gradient shadow">
        <div>
          <b-button 
            type="button" 
            class="btn border rounded p-2" 
            href="/teacher/main/" 
            style="background-color: #f1faa3; color: black;"
          >
            <i class="bi bi-list"> Разделы</i>
          </b-button>
        </div>
        <b-nav-item-dropdown 
          class="border rounded p-2" 
          style="background-color: #f1faa3; font-size: large;" 
          right
        >
          <template #button-content>
            <em>{{ name }}</em>
          </template>
          <b-dropdown-item href="/teacher/profile/">Профиль</b-dropdown-item>
          <b-dropdown-item href="#">Ученики</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar>
    </header>

    <body>
      <b-card v-if="studentData">
        <b-card-body style="position:relative; height:87vh; overflow-y:scroll; text-align: left; font-size: large;">
          <h1>Информация об ученике:</h1>
          <div class="student-info mb-5">
            <p><strong>Имя:</strong> {{ studentData.name }}</p>
            <p><strong>Фамилия:</strong> {{ studentData.surname }}</p>
            <p><strong>Логин:</strong> {{ studentData.login }}</p>
          </div>

          <h2>Результаты тестов:</h2>
          <div v-if="testResults.length > 0">
          <b-table :items="testResults" :fields="resultFields" striped hover>
            <template #cell(test_name)="data">
              {{ data.value }}
            </template>
            
            <template #cell(result)="data">
              {{ data.value }}%
            </template>

            <template #cell(grade)="data">
              {{ calculateGrade(data.value) }}
            </template>
          </b-table>
        </div>
        <div v-else class="no-results-message">
            <div class="empty-results">
                <i class="bi bi-info-circle"></i>
                Ученик еще не проходил тесты
            </div>
        </div>
        </b-card-body>
      </b-card>
    </body>
</template>

<script>
import axios from 'axios';

export default {
  name: 'StudentDetails',
  data() {
    return {
      name: '',
      studentData: null,
      testResults: [],
      resultFields: [
        { key: 'test_name', label: 'Название теста' },
        { key: 'result', label: 'Результат (%)' },
        { key: 'grade', label: 'Оценка' }
      ],
      loading: true,
      error: null
    };
  },
  methods: {
    calculateGrade(percentage) {
      if (percentage > 80) return 5;
      if (percentage > 60) return 4;
      if (percentage > 40) return 3;
      if (percentage > 20) return 2;
      return 1;
    }
  },
  async mounted() {
    try {
      const userData = localStorage.getItem('user');
      this.user = JSON.parse(userData);
      this.name = this.user.name;

      const studentLogin = this.$route.params.login;

      // Загрузка основной информации
      const infoResponse = await axios.get(
        `http://127.0.0.1:8000/users/info/${studentLogin}`
      );
      this.studentData = infoResponse.data;

      // Загрузка результатов тестов
      const resultsResponse = await axios.get(
        `http://127.0.0.1:8000/users/test_result/${studentLogin}`
      );
      const results = resultsResponse.data.result;
      this.testResults = Object.entries(results).map(([test_name, result]) => ({
        test_name,
        result,
        grade: result // Передаем процент для вычисления оценки
      }));

      this.loading = false;
    } catch (error) {
      this.error = error.response?.data?.detail || 'Произошла ошибка при загрузке данных';
      this.loading = false;
    }
  }
};
</script>

<style scoped>
.student-info {
  background-color: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 30px;
}

.student-info p {
  font-size: 1.1rem;
  margin-bottom: 10px;
}
::v-deep .table td {
  transition: background-color 0.3s;
}

::v-deep .table tr:hover td {
  background-color: #f8f9fa !important;
}

.empty-results {
  background-color: rgba(241, 250, 163, 0.3);
  border: 2px solid rgb(241, 250, 163);
  border-radius: 8px;
  padding: 20px;
  margin-top: 15px;
  color: #4a4a4a;
  font-size: 1.1rem;
  display: flex;
  align-items: center;
  gap: 10px;
}

.bi-info-circle {
  font-size: 1.3rem;
  color: #6c757d;
}

.no-results-message {
  margin-top: 20px;
}
</style>