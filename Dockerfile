# Указываем базовый образ
FROM python:3.13

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt ./

# Обновляем pip
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем Poetry
# RUN pip install poetry

# Отключаем создание нового виртуального окружения
# RUN poetry config virtualenvs.create false

# Устанавливаем только зависимости
# RUN poetry install --no-root

# Копируем остальной код приложения
COPY . .

# Указываем порт, на котором будет работать Django (по умолчанию 8000)
EXPOSE 8000

# Команда для запуска Django-сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
