# Базовый образ с Python 3.11, минимальный размер.
FROM python:3.11-slim

# Рабочая директория внутри контейнера.
WORKDIR /app

# Копируем файл зависимостей в контейнер.
COPY requirements.txt ./
# Устанавливаем зависимости без кэша pip.
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный файл приложения.
COPY main.py ./

# Объявляем порт приложения внутри контейнера.
EXPOSE 8000

# Команда по умолчанию для запуска сервера FastAPI.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
