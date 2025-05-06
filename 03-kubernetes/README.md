# Kubernetes-манифесты для развертывания Echo Server

Этот набор манифестов предназначен для запуска приложения Echo Server в кластере Kubernetes.

## Структура файлов

- `namespace.yaml` - Создание отдельного namespace для приложения
- `docker-registry-secret.yaml` - Secret для доступа к приватному Docker-репозиторию
- `deployment.yaml` - Deployment с 3 репликами приложения
- `service.yaml` - Service типа ClusterIP для доступа к подам
- `ingress.yaml` - Опциональный Ingress для внешнего доступа к приложению

## Конфигурация

Перед применением манифестов важно настроить доступ к приватному Docker-репозиторию:

1. Обновите `.dockerconfigjson` в `docker-registry-secret.yaml` с вашими учетными данными:
   ```bash
   kubectl create secret docker-registry docker-registry-secret \
     --docker-server=https://index.docker.io/v1/ \
     --docker-username=goldraven \
     --docker-password=YOUR_PASSWORD \
     --docker-email=YOUR_EMAIL \
     -o yaml --dry-run=client | grep -i data
   ```
   Скопируйте результат в файл `docker-registry-secret.yaml`.

2. При необходимости настройте переменную окружения `AUTHOR` в `deployment.yaml`.

## Применение манифестов

Применяйте манифесты в следующем порядке:

```bash
# 1. Создайте namespace
kubectl apply -f namespace.yaml

# 2. Создайте secret для доступа к приватному репозиторию
kubectl apply -f docker-registry-secret.yaml

# 3. Создайте Deployment и Service
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# 4. (Опционально) Создайте Ingress
kubectl apply -f ingress.yaml
```

## Проверка работоспособности

После применения всех манифестов:

1. Проверьте состояние подов:
   ```bash
   kubectl get pods -n echo-server
   ```

2. Проверьте Service:
   ```bash
   kubectl get svc -n echo-server
   ```

3. Для доступа к сервису без Ingress:
   ```bash
   kubectl port-forward -n echo-server svc/echo-server 8080:80
   ```
   Затем откройте в браузере http://localhost:8080

4. Если вы настроили Ingress, добавьте запись в /etc/hosts:
   ```
   127.0.0.1 echo.example.com
   ```
   И откройте в браузере http://echo.example.com
