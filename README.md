[![Build Status](https://github.com/PivnoyFei/task_for_polimedika/actions/workflows/pol_actions.yml/badge.svg?branch=main)](https://github.com/PivnoyFei/task_for_polimedika/actions/workflows/pol_actions.yml)

<h1 align="center"><a target="_blank" href="">Университет</a></h1>

### Стек: 
![Python](https://img.shields.io/badge/Python-171515?style=flat-square&logo=Python)![3.11](https://img.shields.io/badge/3.11-blue?style=flat-square&logo=3.11)
![FastAPI](https://img.shields.io/badge/FastAPI-171515?style=flat-square&logo=FastAPI)![0.96.0](https://img.shields.io/badge/0.96.0-blue?style=flat-square&logo=0.85.0)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-171515?style=flat-square&logo=PostgreSQL)![14.6](https://img.shields.io/badge/14.6-blue?style=flat-square&logo=13.0)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-171515?style=flat-square&logo=SQLAlchemy)![2.0.15](https://img.shields.io/badge/2.0.15-blue?style=flat-square&logo=13.0)
![Alembic](https://img.shields.io/badge/Alembic-171515?style=flat-square&logo=Alembic)
![Docker](https://img.shields.io/badge/Docker-171515?style=flat-square&logo=Docker)
![Docker-compose](https://img.shields.io/badge/Docker--compose-171515?style=flat-square&logo=Docker)
![GitHub](https://img.shields.io/badge/GitHub-171515?style=flat-square&logo=GitHub)

### Часть 1: База данных
Сначала вам необходимо создать схему базы данных, состоящую из 15 сущностей:

- Студент  # 
- Преподаватель  # 
- Курс  # 
- Группа  # 
- Отделение  # 
- Оценка  # 
- Расписание  # 
- Здание  # 
- Аудитория  # 
- Семестр  # 
- Факультет  # 
- Экзамен  # 
- Задание для самостоятельной работы  # 
- Программа курса  # 
- Учебный план  # 

Ваша задача - создать ER-диаграмму (схему связей между сущностями) и определить свойства каждой из этих сущностей. Затем напишите SQL запросы для создания соответствующих таблиц, включающих все необходимые поля и связи между ними.

#### Мы ждём от вас:

1. ER-диаграмму, которая описывает все сущности и связи между ними.
2. SQL скрипт, который создаёт все таблицы с полями, их типами данных, ключами и связями.
3. Краткое описание каждой сущности и её свойств.
### Часть 2: SQL запросы
Пожалуйста, реализуйте следующие SQL запросы:

1. Выбрать всех студентов, обучающихся на курсе "Математика".
2. Обновить оценку студента по курсу.
3. Выбрать всех преподавателей, которые преподают в здании №3.
4. Удалить задание для самостоятельной работы, которое было создано более года назад.
5. Добавить новый семестр в учебный год.
### Часть 3: FastAPI
Мы бы хотели увидеть следующие точки входа API:

| Метод  | Название | Описание |
|--------|-------   |----------|
| POST   | /students              | - создать нового студента.
| GET    | /students/{student_id} | - получить информацию о студенте по его id.
| PUT    | /students/{student_id} | - обновить информацию о студенте по его id.
| DELETE | /students/{student_id} | - удалить студента по его id.
| GET    | /teachers              | - получить список всех преподавателей.
| POST   | /courses               | - создать новый курс.
| GET    | /courses/{course_id}   | - получить информацию о курсе по его id.
| GET    | /courses/{course_id}/students | - получить список всех студентов на курсе.
| POST   | /grades                       | - создать новую оценку для студента по курсу.
| PUT    | /grades/{grade_id}            | - обновить оценку студента по курсу.

Ожидается реализация этих точек входа API с использованием FastAPI, включая входные и выходные модели Pydantic для каждого маршрута.

### Запуск проекта
Клонируем репозиторий и переходим в него:
```bash
git clone https://github.com/PivnoyFei/task_for_polimedika.git
cd task_for_polimedika
```

### Перед запуском сервера, в папке infra необходимо создать .env файл, с такими же ключами как и .env.template но со своими значениями.

#### Переходим в папку с файлом docker-compose.yaml:
```bash
cd fastapi-project
cd pol-infra
```

### Запуск проекта
```bash
docker-compose up -d --build
```

#### Миграции базы данных (не обязательно):
```bash
docker-compose exec pol-backend alembic revision --message="Initial" --autogenerate
docker-compose exec pol-backend alembic upgrade head
```

#### Останавливаем контейнеры:
```bash
docker-compose down -v
```

#### Автор
[Смелов Илья](https://github.com/PivnoyFei)
