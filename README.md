
# Запуск приложения
Прежде всего установите необходимые зависимости:

```bash
pip install -r requirements.txt
```

В консоли перейдите в папку с проектом и выполните команду создания
папки для данных mongoDB:

```bash
mkdir mongo_data
```

Запустите MongoDB в этой папке:

```bash
mongod --dbpath ./mongo_data
```

Для запуска приложения используйте Uvicorn:

```bash
uvicorn main:app --reload
```
Теперь приложение будет доступно по адресу http://localhost:8000.

