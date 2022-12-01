# Тестовое задание в Фабрику Решений
Задание находится по ссылке: https://www.craft.do/s/n6OVYFVUpq0o6L

Необходимо разработать сервис управления рассылками API администрирования и получения статистики.
## Запуск проекта
1) Клонировать репозиторий:

```
git clone https://github.com/Vendetta-source/fabrique_test_task.git
```

2) Создать виртуальное окружение:

```
python -m venv venv
```

3) Активировать окружение:

Windows: 
```
venv/scripts/activate
```

Linux: 
```
source\venv\bin\activate
```

4) Установить зависимости:

```
pip install -r requirements.txt
```

5) В файле settings.py заполнить необходимые данные.

6) Создать и применить миграции БД:

```
python manage.py makemigrations
python manage.py migrate
```

7) Запустить сервер:

```
python manage.py runserver
```

-----
## Реализованы дополнительные пункты

Пункт 5: по адресу /docs/ открывается страница со Swagger UI и в нём отображается описание разработанного API.

Пункт 6: реализован администраторский Web UI для управления рассылками и получения статистики по отправленным сообщениям.
