### Описание:
API для Yatube

### Установка:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:OlegPrizov/api_final_yatube.git
```

```
cd api_final_yatube
```

Установить зависимости:

```
pip install -r requirements.txt
```

Запустить проект:

```
python manage.py runserver
```

### Примеры запросов:

Получение публикаций
Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией.

```
http://127.0.0.1:8000/api/v1/posts/
```
вернет
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

Получение комментариев
Получение всех комментариев к публикации.

```
http://127.0.0.1:8000/api/v1/posts/
```
вернет
```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```
и так далее