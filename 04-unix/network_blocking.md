## Запуск контейнера
1. Запуск контейнера:
```bash
docker run -it --rm ubuntu -- bash
```

2. Проверка доступа в сеть:
```bash
apt-get update
```
Результат: команда выполняется успешно, есть доступ в интернет.

## Способ 1: Блокировка с помощью iptables

1. Установка iptables:
```bash
apt-get install -y iptables
```

2. Блокировка исходящего трафика:
```bash
iptables -P OUTPUT DROP
```

3. Проверка результата:
```bash
apt-get update
```

## Способ 2: Блокировка через настройку маршрутизации

1. Удаление маршрута по умолчанию:
```bash
ip route del default
```

2. Проверка результата:
```bash
apt-get update
```

