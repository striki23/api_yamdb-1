# Проект **YAMBD**
### **Описание проекта:**
*Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.*
*Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).* 
*Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).* 
*Добавлять произведения, категории и жанры может только администратор.*
*Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.*
*Пользователи могут оставлять комментарии к отзывам.*
*Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.*

---

### **Технологии:**
Python 3.7 <br>
Django 3.2 <br>
DRF 3.12.4 <br>
JWT

---

### **Команда разработчиков:**
- Менеджер Ольга Рогачева
- Ришат https://github.com/Rishat-Ver
- Даша https://github.com/striki23
- Сергей https://github.com/code-nf

---

### **Запуск проекта:**
- python -m venv venv (Устанавливаем виртуальное окружение)
- source venv/Scripts/activate (Активируем виртуальное окружение)
- python -m pip install --upgrade pip (Обновляем pip)
- pip install -r requirements.txt (Устанавливаем зависимости)
- python manage.py migrate (Делаем миграции)
- python manage.py runserver (Запускаем проект)

---

### **Примеры работы с api:**
***Документация:*** http://127.0.0.1:8000/redoc/

**Алгоритм регистрации пользователей**
- Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами email и username на эндпоинт /api/v1/auth/signup/.
- YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email.
- Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт /api/v1/auth/token/, в ответе на запрос ему приходит token (JWT-токен).
- При желании пользователь отправляет PATCH-запрос на эндпоинт /api/v1/users/me/ и заполняет поля в своём профайле (описание полей — в документации).


**Пользовательские роли**
- Аноним — может просматривать описания произведений, читать отзывы и комментарии.
- Аутентифицированный пользователь (user) — может, как и Аноним, читать всё, дополнительно он может публиковать отзывы и ставить оценку произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы; может редактировать и удалять свои отзывы и комментарии. Эта роль присваивается по умолчанию каждому новому пользователю.
- Модератор (moderator) — те же права, что и у Аутентифицированного пользователя плюс право удалять любые отзывы и комментарии.
- Администратор (admin) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
- Суперюзер Django — обладет правами администратора (admin)


**Примеры работы с url api:**
Регистрация нового пользователя POST http://127.0.0.1:8000/api/v1/auth/signup/ <br>
Права доступа: Доступно без токена. <br>
Запрос:
```
{
    "email": "user@example.com",
    "username": "string"
}
```
Ответ:
```
{
    "email": "string",
    "username": "string"
}
```

Получение JWT-токена POST http://127.0.0.1:8000/api/v1/auth/token/ <br>
Права доступа: Доступно без токена. <br>
Запрос:
```
{
    "username": "string",
    "confirmation_code": "string"
}
```
Ответ:
```
{
    "token": "string"
}
```

Получение списка всех категорий GET http://127.0.0.1:8000/api/v1/categories/ <br>
Права доступа: Доступно без токена <br>
Ответ:
```
{
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
        {}
    ]   
}
```

Добавление новой категории POST http://127.0.0.1:8000/api/v1/categories/ <br>
Права доступа: Администратор. <br>
Запрос:
```
{
    "name": "string",
    "slug": "string"
}
```
Ответ:
```
{
    "name": "string",
    "slug": "string"
}
```

Удаление категории DELETE http://127.0.0.1:8000/api/v1/categories/{slug}/ <br>
Права доступа: Администратор. <br>

Получение списка всех комментариев к отзыву GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/ <br>
Права доступа: Доступно без токена. <br>
Ответ:
```
{
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
        {
            "id": 0,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ]
}
```

Добавление комментария к отзыву POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/ <br>
Права доступа: Аутентифицированные пользователи. <br>
Запрос:
```
{
    "text": "string"
}
```
Ответ:
```
{
    "id": 0,
    "text": "string",
    "author": "string",
    "pub_date": "2019-08-24T14:15:22Z"
}
```

---

Данный проект , является совместной работой трех начинающих разроботчиков (Ришат , Даша , Сергей) <br>
Он сделан в рамках обучения на курсе Python-рфзроботчик Яндекс-Практикума
