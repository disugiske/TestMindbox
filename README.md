## Тестовое задание MindBox

### Задание №1
```
Есть Pandas DataFrame со столбцами [“customer_id”, “product_id”, “timestamp”], который содержит данные по просмотрам товаров на сайте. Есть проблема – просмотры одного customer_id не разбиты на сессии (появления на сайте). Мы хотим разместить сессии так, чтобы сессией считались все смежные просмотры, между которыми не более 3 минут.

Написать методом который создаст в Pandas DataFrame столбец session_id и проставит в нем уникальный int id для каждой сессии.

У каждого пользователя может быть по несколько сессий. Исходный DataFrame может быть большим – до 100 млн строк.
```

Файл с решением находится в /pandas_task/unique_id.py

Так же в папке есть файл generate_csv.py - с его помощью можно создать произвольное количество рандомных данных для теста


### Задание №2
```
В SQL базе данных есть продукты и категории. Одному продукту может соответствовать много категорий, в одной категории может быть много продуктов.

Напишите HTTP API через которое можно получить:

- список всех продуктов с их категориями,
- список категорий с продуктами,
- список всех пар «Имя продукта – Имя категории».

Если у продукта нет категорий, то он все равно должен выводиться.
Если у категории нет продуктов, то она все равно должна выводиться.
Проект должен содержать docker-compose.yml файл, через который можно запустить сервис и проверить его работу.
```
#### Проект задеплоен на http://89.223.69.51:9000/
## Методы:
- /api/v1/all - список всех продуктов с их категориями
- /api/v1/category - список категорий с продуктами
- /api/v1/pair - список всех пар «Имя продукта – Имя категории»
- /docs - Swagger

- Предусмотрен метод автоматически напоняющий базу данных случаными словами,
для этого надо перейти по адресу

/add?cat=5&prod=10 ,
где cat - количество категорий, prod - количество продуктов

### .env файл оставлен специально, чтобы было проще проверять

## API собран в Docker Build запускается по команде:
```
make prod
```
Или если не установлен make:
```
docker-compose -f docker-compose.yaml up -d --build
```
Сервер будет доступен на 8000 порту localhost

### После запуска выполните миграции:
```
make migrate
```
Или
```
docker-compose -f docker-compose.yaml exec web alembic upgrade head
```
### Остановка:
```
make down
```
Или
```
docker-compose -f docker-compose.yaml down
```

