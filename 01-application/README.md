# Echo Server

Простое веб-приложение, которое отображает информацию о хосте:
- Имя хоста
- IP-адрес хоста
- Имя автора (передаётся через переменную окружения `AUTHOR`)

## Запуск приложения локально

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Запустите приложение:
```bash
python app.py
```

3. Откройте в браузере: http://localhost:8000

## Запуск через Docker

1. Сборка образа:
```bash
docker build -t your_username/echo-server:latest .
```

2. Запуск контейнера с указанием имени автора:
```bash
docker run -p 8000:8000 -e AUTHOR="Ваше имя" your_username/echo-server:latest
```

3. Откройте в браузере: http://localhost:8000

## Публикация образа в Docker Hub

1. Войдите в Docker Hub:
```bash
docker login
```

2. Соберите образ (используйте своё имя пользователя):
```bash
docker build -t your_username/echo-server:latest .
```

3. Опубликуйте образ:
```bash
docker push your_username/echo-server:latest
```

## Команды для управления контейнерами

1. Просмотр запущенных контейнеров:
```bash
docker ps
```

2. Остановка контейнера:
```bash
docker stop <container_id_или_name>
```

3. Удаление контейнера:
```bash
docker rm <container_id_или_name>
```

4. Принудительное удаление (даже запущенного):
```bash
docker rm -f <container_id_или_name>
```
