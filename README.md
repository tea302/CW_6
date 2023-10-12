# coursework_5
# Курс 6. Курсовая

![Screenshot 2022-03-14 at 15.10.20.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c17e02fe-78e5-40c9-aefb-07f7c3f09f92/Screenshot_2022-03-14_at_15.10.20.png)

https://github.com/skypro-008/coursework_6_skymarket.git

Данная курсовая работа представляет собой backend-часть для сайта объявлений. 

Frontend-часть уже готова.

[demo.mp4](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3366c84d-8e90-479a-b622-4f722fcd5dc2/demo.mp4)

Бэкенд-часть проекта предполагает реализацию следующего функционала:

- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- Восстановление пароля через электронную почту (не обязательно).
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
- Под каждым объявлением пользователи могут оставлять отзывы.
- В заголовке сайта можно осуществлять поиск объявлений по названию.

**Краткое техническое задание и рекомендации по порядку выполнения:**

- **Этап I.** Настройка Django-проекта.
    
    На данном этапе нам предстоит подготовить наш Django-проект к работе.
    Данный этап состоит из трех подзадач:
    
    1. Подключение базы данных Postgres.
    2. Подключение CORS headers.
    3. Подключение Swagger.
- **Этап II.** Создание модели юзера. Настройка авторизации и аутентификации.
    - Создание модели пользователя.
        - Необходимые поля:
        - first_name — имя пользователя (строка).
        - last_name — фамилия пользователя (строка).
        - phone — телефон для связи (строка).
        - email — электронная почта пользователя (email) **(используется в качестве логина).**
        - role — роль пользователя, доступные значения: user, admin.
        - image - аватарка пользователя
    - Настройка авторизации и аутентификации.
        
        На данном этапе мы будем настраивать авторизацию пользователя с помощью библиотеки simple_jwt. Подробнее об этом можно узнать в рекомендациях
        
    - Сброс и восстановление пароля через почту* (необязательно).
        
        Основная сложность при настройке сброса и восстановления пароля через почту — подключение самого почтового ящика, через который будет происходить отправка таких сообщений. Как правило, при такой настройке требуется разрешить доступ неавторизованным приложениям к используемому почтовому ящику — эти настройки обычно находятся в разделе «Безопасность» на сайтах почтовых сервисов.
        В целом логика сброса пароля с использованием Djoser достаточно проста.
        
        1. Юзер отправляет POST-запрос на адрес 
        
        `/users/reset_password/` с содержанием: 
            
            ```json
            {
                "email": "example@mail.com"
            } 
            ```
            
        2. Сервер высылает на почту ссылку вида:
            
            ```html
            "/<url>/{uid}/{token}" # предварительно это настраивается в settings
            ```
            
        3. Далее идет работа фронта — из данной ссылки парсится uid и токен, который впоследствии передается в JSON вместе с новым паролем на адрес `users/reset_password_confirm` — по умолчанию он выглядит именно так.
        А содержание POST-запроса, отправляемого на бэкэнд, выглядит следующим образом:
            
            ```json
            {
                "uid": "uid",
                "token": "token"
                "new_password": "P4$$W0RD"
            }
            ```
            
- **Этап III.** Описание моделей объявлений и отзывов.
    
    Модель **объявления** должна содержать следующие поля:
    
    - title — название товара.
    - price — цена товара (целое число).
    - description — описание товара.
    - author — пользователь, который создал объявление.
    - created_at — время и дата создания объявления.
    
    *Все записи при выдаче должны быть отсортированы по дате создания 
    (чем новее, тем выше).*
    
    Модель **отзыва** должна содержать следующие поля:
    
    - text — текст отзыва.
    - author — пользователь, который оставил отзыв.
    - ad — объявление, под которым оставлен отзыв.
    - created_at - время и дата создания отзыва
- **Этап IV.** Создание views и эндпоинтов.
    
    Для получения документации по требуемым эндпоинтам выполните команду `python3 manage.py runserver` в cклонированном репозитории,
    откройте браузер и перейдите по адресу:
    `[http://localhost:8000/api/redoc-tasks/](http://127.0.0.1:8000/api/redoc-tasks/)`
    
    Задание со звездочкой* (не обязательно)
    
    Также наша работа предусматривает реализацию поиска товаров на главной странице по названию. Для выполнения данного  задания рекомендуем использовать библиотеку `django-filter`. С документацией можно ознакомиться здесь: https://django-filter.readthedocs.io/en/stable/guide/install.html. В рекомендациях есть краткая инструкция по использованию фильтров.
    
    Также обратите внимание на эндпоинты, которые требуют реализации пагинации. Эндпоинт /ads/ требует не более 4 объектов на странице (ограничение фронта)
    
- **Этап V**. Определение permissions к views.
    
    **Анонимный пользователь может**:
    
    получать список объявлений.
    
    **Пользователь может:**
    
    - получать список объявлений,
    - получать одно объявление,
    - создавать объявление
    - редактировать и удалять свое объявление,
    - получать список комментариев,
    - создавать комментарии,
    - редактировать/удалять свои комментарии.
    
    **Администратор может:**
    
    дополнительно к правам пользователя редактировать или удалять
    объявления и комментарии любых других пользователей.
    

Что будет в прекоде проекта:

- Шаблон вашего Django-проекта.
- Фикстуры для будущих моделей.
    
    В фикстурах представлено несколько моделей пользователей для поведения тестов. Логин пользователя вы можете посмотреть сами, а в качестве пароля используйте “111”
    

**Рекомендации** **по реализации проекта:**

- Рекомендации при выполнении этапа I.
    - Первое, с чего необходимо начать, — это подключить базу данных к нашему проекту. Делается это с помощью добавления свойства DATABASE к [settings.py](http://settings.py). Пример подключения такой базы можно подсмотреть в документации (https://docs.djangoproject.com/en/4.0/ref/settings/#databases) или же в любом из тренажеров.
    - Следующим шагом будет подключение приложения для генерации документации к нашему проекту (Swagger). Воспользуйтесь знаниями, полученными на уроках, а также документацией.
    Для генерации документации можете воспользоваться одной из следующих библиотек:
    - [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/index.html)
    - [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/)
    - Также неотъемлемой частью почти каждого проекта является подключение ****CORS для нашего публичного API. Для настройки можно воспользоваться библиотекой `django-cors-headers`. Помимо уроков, здесь есть документация по установке: https://pypi.org/project/django-cors-headers/.
    - Также обратите внимание что в прекоде проекта находится файл .env.example — здесь хранятся данные, которые не следует выкладывать на GitHub. Например, логин и пароль от электронной почты, который используется вашим приложением.
    Чтобы локально воспользоваться этими переменными, рекомендуем использовать библиотеку python-dotenv. Подробно документацию можно посмотреть здесь: https://pypi.org/project/python-dotenv/.
- Рекомендации по выполнению этапа II.
    
    При создании модели пользователя и авторизации в данном проекте рекомендуем попробовать воспользоваться расширением для Django — Djoser (https://djoser.readthedocs.io/en/latest/).
    
    Данная библиотека позволяет практически из коробки реализовать CRUD для модели пользователя.
    
    Ключевые моменты для использования Djoser:
    
    - **установка**: >>> pip install djoser
    - **добавление библиотеки в константу INSTALLED_APPS** в модуле settings (данная библиотека должна идти по порядку после приложения Django.auth):
    
    ```python
    INSTALLED_APPS = [
        "django.contrib.auth",
        ...
        "djoser"
        ...
    ]
    ```
    
    - **настройка Djoser:** также производится в модуле [settings.py](http://settings.py) в константе DJOSER. В данном случае нас интересуют следующие настройки:
    
    ```python
    DJOSER = {
        'SERIALIZERS': {
            'user_create': 'users.serializers.UserRegistrationSerializer'
        },
        'LOGIN_FIELD': 'email'
    }
    ```
    
    В Djoser есть еще много опций, которые подлежат настройке, — здесь же мы определили, что используем кастомный  serializer для создания пользователя (пригодится нам в дальнейшем), а также поле, через которое пользователь аутентифицируется (login).
    
    Помимо вышеперечисленных настроек, в нашем случае для корректной работы Djoser потребуется кастомная модель пользователя. Что нам и предстоит сделать в следующем шаге.
    
    Перейдем в приложение users в модуль models.py и создадим нашего пользователя. Пользователь должен быть унаследован от модели AbstractBaseUser:
    
    ```python
    from django.contrib.auth.models import AbstractBaseUser 
    ```
    
    Очень подробно об этом описывается в [документации](https://djoser.readthedocs.io/en/latest/). Мы же выделим только ключевые моменты. Помимо полей, определенных в кратком ТЗ, в нашей модели должны быть предопределены методы для корректной работы встроенной системы пермишенов и аутентификации пользователя.
    
    ```python
    class User(AbstractBaseUser)
    # Необходимые параметры для корректной работе Django
        @property
        def is_superuser(self):
            return self.is_admin
    
        @property
        def is_staff(self):
            return self.is_admin
    
        def has_perm(self, perm, obj=None):
            return self.is_admin
    
        def has_module_perms(self, app_label):
            return self.is_admin
        
        # также для работы модели пользователя должен быть переопределен
        # менеджер объектов
        objects = UserManager()
    ```
    
    - Подсказка
        
        ```python
        # В качестве подсказки — эти поля имеют
        # непосредственное отношение именно к нашей модели
        
            
        
            # эта константа определяет поле для логина пользователя
            USERNAME_FIELD = 'email' 
        
            # эта константа содержит список с полями, 
            # которые необходимо заполнить при создании пользователя
            REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"] 
            
            # для корректной работы нам также необходимо 
            # переопределить менеджер модели пользователя
        
            objects = UserManager()
            @property
            def is_admin(self):
                return self.role == UserRoles.ADMIN # 
        
            @property
            def is_user(self):
                return self.role == UserRoles.USER
        ```
        
    
    Как должен выглядеть простейший менеджер для нашего пользователя
    
    ```python
    # Менеджер должен быть унаследован от следующего класса
    from django.contrib.auth.models import BaseUserManager
    
    # Менеджер должен содержать как минимум две следующие функции
    class UserManager(BaseUserManager):
        """
        функция создания пользователя — в нее мы передаем обязательные поля
        """
        def create_user(self, email, first_name, last_name, phone, password=None):
            if not email:
                raise ValueError('Users must have an email address')
            user = self.model(
                email=self.normalize_email(email),
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                role="user"
            )
            user.is_active=True
            user.set_password(password)
            user.save(using=self._db)
    
            return user
    
        def create_superuser(self, email, first_name, last_name, phone, password=None):
            """
            функция для создания суперпользователя — с ее помощью мы создаем админинстратора
            это можно сделать с помощью команды createsuperuser
            """
    
            user = self.create_user(
                email,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                password=password,
                role="admin"
            )
            
            user.save(using=self._db)
            return user
    ```
    
    Основная подготовка менеджера готова, осталось только добавить необходимые urls.
    
    *Заметим, что определять views в нашем случае необязательно — Djoser делает это из коробки.*
    
    ```python
    from django.urls import include, path
    from djoser.views import UserViewSet
    from rest_framework.routers import SimpleRouter
    
    users_router = SimpleRouter()
    
    # обратите внимание, что здесь в роуте мы регистрируем ViewSet,
    # который импортирован из приложения Djoser
    users_router.register("users", UserViewSet, basename="users")
    
    urlpatterns = [
        path("", include(users_router.urls)),
    ]
    
    ```
    
    Что мы получаем в итоге? Все необходимые urls для управления пользователями, а именно:
    
    ```python
    GET "users/" — список профилей пользователей
    POST "users/" — регистрация пользователя
    GET, PATCH, DELETE "users/{id}" — в соотвествии с REST и необходимыми permissions (для администратора)
    GET PATCH "users/me" — получение и изменение своего профиля
    POST "users/set_password" — ручка для изменения пароля
    POST "users/reset_password" — ручка для направления ссылки сброса пароля на email*
    POST "users/reset_password_confirm" — ручка для сброса своего пароля*
    
    ```
    
    Две последние ручки — это задание со звездочкой. Подробности можно поискать в официальной документации. На frontend-части проекта эти возможности также предусмотрены.
    
    В целом этого функционала нам будет достаточно, однако в Swagger который вы подключите, будет еще много других полезных функций «из коробки».
    Их полный список можно посмотреть здесь: https://djoser.readthedocs.io/en/latest/base_endpoints.html.
    
    Помимо пользователя, осталось подключить авторизацию по токену.
    
    Это также можно сделать с помощью Djoser, однако оставим это для самостоятельного изучения и выберем простой вариант — использование библиотеки `djangorestframework-simplejwt`. 
    
    **Ключевой момент:** не забудьте добавить соответствующие настройки в settings.py.
    
    ```python
    REST_FRAMEWORK = {
        "DEFAULT_AUTHENTICATION_CLASSES": (
            "rest_framework_simplejwt.authentication.JWTAuthentication",
        ),
    }   
    ```
    
- Рекомендации по выполнению этапа III.
    
    Этап создания моделей представляется как наиболее простая часть проекта.
    
    При этом и здесь следует выделить ключевые моменты.
    
    Обратите внимание, что поле image хранит в себе файл с картинкой и для правильного отображения этой картинки необходимо внести 2 переменные в файл settings.py, а именно: MEDIA_URL и MEDIA_ROOT. Подробности об этом предлагаем вам поискать в документации.
    
    Кроме того, наш проект предполагает локальный запуск на сервере. Следовательно, необходимо, чтобы сервер правильно перенаправлял ссылки на файлы с картинками — это можно решить, если добавить к списку urlpatterns в файле [urls.py](http://urls.py) в директории skymarket следующую строку:
    
     `urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`
    
- Рекомендации по выполнению этапа IV.
    
    В первую очередь, еще раз внимательно ознакомьтесь с интерактивной документацией. Она расположена по адресу `[http://localhost:8000/api/redoc-tasks/](http://127.0.0.1:8000/api/redoc-tasks/)`
    
    Здесь практически всё, что необходимо знать при настройке view-функций и urls.
    
    Также предполагается, что определенные сложности могут возникнуть при сериализации данных, а также выборе QuerySet для ClassBasedViews (CBV).
    
    Не забывайте, что CBV имеют методы `perform_create`, `perform_update`, которые могут быть использованы для добавления дополнительных значений, требуемых для создания модели, например пользователя.
    (`self.request.user`).
    
    Также существуют методы `get_queryset` и `get_serializer_class` для изменения QuerySet и сериалайзера CBV в зависимости от исполняемого в CBV action-действия.
    
    - Подсказка
        
        Стандартные экшены, используемые view-классами:
        
        - list
        - retrieve
        - create
        - destroy
        - update
        - partial_update
    
    Использование `django-filter` (не обязательно).
    
    **Краткая инструкция для настройки простого фильтра**
    
    Сначала, как и в случае с Djoser, необходимо подключить Django-filter к нашему Django-приложению, для этого нужно добавить его в INSTALLED_APPS модуля [settings.py](http://settings.py):
    
    ```python
    INSTALLED_APPS = [
        ...
        'django_filters',
    ]
    ```
    
    Как настроить фильтры?
    
    Настройка фильтров с помощью нашей библиотеки осуществляется в 2 шага.
    
    - **Шаг 1. Описываем сам фильтр.**
        
        Как правило, у каждого Django-приложения свои фильтры — и они хранятся в файле filters.py в корне папки конкретного приложения.
        
        Разберем простой класс фильтра на примере:
        
        ```python
        import django_filters
        from my_app.models import Mymodel
        
        # Фильтры в Django базируются на основе моделей
        
        class MyModelFilter(django_filters.rest_framework.FilterSet):
            title = django_filters.CharFilter(field_name="title", lookup_expr="icontains", )
            
            # CharFilter — специальный фильтр, который позволяет искать совпадения в текстовых полях модели
            class Meta:
                model = Mymodel
                fields = ("title", )
        ```
        
        Аргумент `title` в данном случае представляет собой название query-параметра, по которому будет осуществляться поиск.
        Например, при запросе на адрес `http://localhost:8000/all_items/?title=кот` произойдет поиск всех записей в БД, у которых в тексте встречается сочетание букв «кот» (пример дан как образец, в проекте используйте url из документации).
        
        `CharFilter` — специальный фильтр, позволяет искать совпадения в текстовых полях модели. Таких фильтров в Django-filters существует много — подробнее обо всех можно узнать в официальной документации.
        
        Аргумент `field_name` — поле модели, по которому производится поиск.
        
        Аргумент `lookup_expr` — тип поиска в CharField. Обо всех возможных используемых полях можно почитать в документации (https://docs.djangoproject.com/en/4.0/ref/models/querysets/#field-lookups-1), а нам пригодится именно `icontains`.
        
        Далее идет класс `Meta`.
        
        Здесь мы определяем нашу модель, а также поля модели, по которым будем осуществлять поиск.
        
    - **Шаг 2. Подключение фильтра к class-based view**
        
        Для этого нам необходимо указать: 
        
        ```python
        from django_filters.rest_framework import DjangoFilterBackend
        from my_app.filters import MyModelFilter
        
        class MyModelViewSet(viewsets.ModelViewSet):
            filter_backends = (DjangoFilterBackend,) # Подключаем библотеку, отвечающую за фильтрацию к CBV
            filterset_class = MyModelFilter # Выбираем наш фильтр
        ```
        
        Готово! Фильтр должен работать.
        
- Рекомендации по выполнению этапа V.
    
    Приступать к этому этапу следует, когда вы уже удостоверились в работоспособности своих эндпоинтов и проверили их с помощью Postman.
    
    Реализация пермишенов в Django также имеет свои особенности. 
    
    В целом, в нашем случае их реализация не многим отличается от предыдущего этапа — используйте функцию `get_permissions`, а выбор пермишенов также можно установить в зависимости от исполняемого в СBV action-действия.
    
- Дополнительная информация, необходимая для реализации проекта.