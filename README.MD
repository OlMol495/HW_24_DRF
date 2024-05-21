Запуск проекта с помощью Docker Compose
Для запуска проекта с помощью Docker Compose выполните следующие шаги:

Установите Docker и Docker Compose, если они еще не установлены на вашем компьютере.

Сборка образов
docker-compose build

Запуск контейнеров
docker-compose up

Запуск контейнеров в фоне
docker-compose up -d

Сборка образа и запуск в фоне после успешной сборки
docker-compose up -d —build

Выполнение команды внутри контейнера
docker-compose exec <app> <command>

Откройте браузер и перейдите по адресу http://localhost:8000 для доступа к проекту.
