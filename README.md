# Проект на базе Django Rest Framework, где каждый может создавать и размещать свои полезные привычки.

## Установка:
1. Клонируйте репозиторий:
```git clone git@github.com:```
2. Установите библиотеки из requirements.txt:
```pip install -r requirements.txt```
3. Создайте файл .env в корне проекта и добавьте туда необходимые переменные окружения, указанные в файле .env.sample.

### Подготовка к запуску и запуск проекта:
1. Установите Docker Desktop для вашей операционной системы и запустите его.
2. Запустите Redis
3. В терминале, перейдите в директорию проекта. 
4. Запустите команду: docker-compose up -d --build

После запуска веб-приложение будет доступно по адресу: http://127.0.0.1:8000
IP адрес сервера ВМ: 130.193.44.35

### Проект разворачивается через GitHub Actions
Создайте следующие секреты: SSH_USER, SSH_KEY, SERVER_IP, DOCKER_HUB_USERNAME, DOCKER_HUB_ACCESS_TOKEN, SECRET_KEY, DEPLOY_DIR

### Проект использует docker-compose для запуска всех сервисов
Запуск
``` docker-compose up -d --duild ```
Остановка
``` docker-compose down ```