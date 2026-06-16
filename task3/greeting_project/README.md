# Кейс-задача №3. Веб-приложение на Django

Простое веб-приложение, которое позволяет пользователю ввести своё имя
и получить персонализированное приветствие на главной странице.

## Функциональность
- Главная страница с формой ввода имени и кнопкой "Submit".
- Модель `Greeting` с единственным полем `name` (плюс служебное `created_at`),
  хранящая введённые имена в базе данных.
- Обработка формы: имя сохраняется в БД и отображается как приветствие.
- Обработка ошибок: пустое поле имени не проходит валидацию формы,
  пользователю показывается сообщение об ошибке.
- Стилизация интерфейса через CSS (градиентный фон, скруглённые элементы).
- Защита от CSRF обеспечена встроенным `CsrfViewMiddleware` и тегом
  `{% csrf_token %}` в шаблоне формы.

## Структура проекта
```
greeting_project/
├── manage.py
├── requirements.txt
├── greeting_project/      # настройки проекта
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── greetings/              # приложение
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    ├── migrations/
    ├── templates/greetings/index.html
    └── static/greetings/style.css
```

## Установка и запуск
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Приложение будет доступно по адресу http://127.0.0.1:8000/

## Репозиторий
Ссылка на GitHub-репозиторий: https://github.com/krosh2807/synergy_practika
