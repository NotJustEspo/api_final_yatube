## Проект YaTube
Проект YaTube - это блог-сервис, который предполгает возможность зарегистрироваться, создать, отредактировать или удалить свой пост, прокомментировать пост другого автора и подписаться на него.

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone# git@github.com:NotJustEspo/api_final_yatube.git
```

Перейти в директорию с проектом:

```
cd api_final_yatube
```

Создать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt

```
python3 -m pip install --upgrade pip
```

```
python3 manage.py -r requirements.txt
```

Выполнить миграцию:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры запросов к API:

### Пример 1. POST-запрос на создание поста.

POST api/v1/posts/

### Пример 2. PATCH-запрос на частичное обновление поста.

PATCH api/v1/posts/{id}

### Пример 3. GET-запрос на получение комментариев.

GET api/v1/posts/{post_id}/comments/

### Пример 4. DELETE-запрос на удаление комментария.

DELETE api/v1/posts/{post_id}/comments/{id}/

### Пример 5. GET-запрос на получение всех подписок пользователя.

GET api/v1/follow/
