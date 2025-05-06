## 1. Авторизация в Docker Hub
```bash
docker login
```
## 2. Сборка образа
```bash
# Сборка с использованием имени пользователя goldraven
docker build -t goldraven/echo-server:latest .
```
## 3. Публикация образа в приватный регистр Docker Hub
```bash
docker push goldraven/echo-server:latest
#можно добавить версию тегом
docker tag goldraven/echo-server:latest goldraven/echo-server:v1.0
#команда для публикации образа с тегом
docker push goldraven/echo-server:v1.0
```
## 4. Команды для запуска Docker образа
```bash
# запуск докер контейнера
docker run -p 8000:8000 goldraven/echo-server:latest

# Запуск с автоматическим перезапуском при сбоях
docker run -d -p 8000:8000 --restart unless-stopped goldraven/echo-server:latest
```