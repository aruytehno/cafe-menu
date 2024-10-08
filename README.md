# Café Menu

## Описание
Это проект на Django для создания интерактивного меню кофейни. Он позволяет управлять элементами меню и отображать их на веб-странице.

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/aruytehno/cafe-menu.git
cd cafe-menu

```
   
2. Создайте виртуальное окружение:
```bash
python3 -m venv venv
```

3. Активируйте виртуальное окружение:
- ```bash
   source venv/bin/activate # Mac
  ```

- ```bash
  venv\Scripts\activate # Windows
  ```

4. Обновите пакеты:
```bash
pip install --upgrade pip
```

5. Установите зависимости:
```bash
pip install -r requirements.txt
```
6. Соберите статические файлы (если требуется):
```bash
python manage.py collectstatic
```
7. Создание миграции для БД:
```bash
python manage.py makemigrations
python manage.py migrate
```

8. Загрузите данные в базу:
```bash
python manage.py loaddata menu.json
```

9. Создайте суперпользователя (если необходимо использовать админ-панель):
```bash
python manage.py createsuperuser
```

10. Запустите локальный сервер:
```bash
python manage.py runserver
```


## Полезности:
#### Регулярки для обрамления ссылок в проекте
###### В поле "Найти" вставьте регулярное выражение:
```txt
assets/img/([^'\s]+\.jpg)
```
###### В поле "Заменить на" вставьте:
```txt
{% static 'assets/img/$1' %}
```



## Что можно дополнительно реализовать в проекте
- [ ] Добавление изображения блюда
- [ ] Отдельную панель администратора
- [ ] QR - коды столиков с возможностью сделать сразу заказ или позвать официанта
- [ ] Сделать API на Django REST Framework (DRF)
- [ ] Добавить ночной и дневной режим в админку для барменов и официантов
- [ ] Добавить ночной и дневной режим на сайт для удобства посетителей