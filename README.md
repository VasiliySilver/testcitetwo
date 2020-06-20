
# Урок 2 | Установка виртуального окружения
====================================
# Windows
python -m venv venv

# Linux
python3 -m venv venv

Активация виртуального окружения

# Windows
.\venv\Scripts\activate

# Linux
source venv/bin/activate


# Урок 3 | Установка Django
====================================

###### перед установкой django добавим .gitignore

                # Byte-compiled / optimized / DLL files
                __pycache__/
                *.py[cod]
                *$py.class
                
                # C extensions
                *.so
                
                # Distribution / packaging
                .Python
                build/
                develop-eggs/
                dist/
                downloads/
                eggs/
                .eggs/
                lib/
                lib64/
                parts/
                sdist/
                var/
                wheels/
                share/python-wheels/
                *.egg-info/
                .installed.cfg
                *.egg
                MANIFEST
                
                # PyInstaller
                #  Usually these files are written by a python script from a template
                #  before PyInstaller builds the exe, so as to inject date/other infos into it.
                *.manifest
                *.spec
                
                # Installer logs
                pip-log.txt
                pip-delete-this-directory.txt
                
                # Unit test / coverage reports
                htmlcov/
                .tox/
                .nox/
                .coverage
                .coverage.*
                .cache
                nosetests.xml
                coverage.xml
                *.cover
                *.py,cover
                .hypothesis/
                .pytest_cache/
                cover/
                
                # Translations
                *.mo
                *.pot
                
                # Django stuff:
                *.log
                local_settings.py
                db.sqlite3
                db.sqlite3-journal
                
                # Flask stuff:
                instance/
                .webassets-cache
                
                # Scrapy stuff:
                .scrapy
                
                # Sphinx documentation
                docs/_build/
                
                # PyBuilder
                .pybuilder/
                target/
                
                # Jupyter Notebook
                .ipynb_checkpoints
                
                # IPython
                profile_default/
                ipython_config.py
                
                # pyenv
                #   For a library or package, you might want to ignore these files since the code is
                #   intended to run in multiple environments; otherwise, check them in:
                # .python-version
                
                # pipenv
                #   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
                #   However, in case of collaboration, if having platform-specific dependencies or dependencies
                #   having no cross-platform support, pipenv may install dependencies that don't work, or not
                #   install all needed dependencies.
                #Pipfile.lock
                
                # PEP 582; used by e.g. github.com/David-OConnor/pyflow
                __pypackages__/
                
                # Celery stuff
                celerybeat-schedule
                celerybeat.pid
                
                # SageMath parsed files
                *.sage.py
                
                # Environments
                .env
                .venv
                env/
                venv/
                ENV/
                env.bak/
                venv.bak/
                
                # Spyder project settings
                .spyderproject
                .spyproject
                
                # Rope project settings
                .ropeproject
                
                # mkdocs documentation
                /site
                
                # mypy
                .mypy_cache/
                .dmypy.json
                dmypy.json
                
                # Pyre type checker
                .pyre/
                
                # pytype static type analyzer
                .pytype/
                
                # Cython debug symbols
                cython_debug/
                
                .idea/



pip install Django

django-admin startproject mysite

python manage.py runserver
python manage.py runserver 4000
python manage.py runserver 1.2.3.4:4000


# Урок 4 | Приложения в Django
====================================

cd mysite
python manage.py startapp news

add to >mysite/settings.py

                INSTALLED_APPS = [
                    'django.contrib.admin',
                    'django.contrib.auth',
                    'django.contrib.contenttypes',
                    'django.contrib.sessions',
                    'django.contrib.messages',
                    'django.contrib.staticfiles',
                    'news.apps.NewsConfig',
                ]



# Урок 5 | MVC Model Views Controller
====================================
В Django MTV

Model = Model
Views = Template
Conntroller = View

В Django MTV


# Урок 6 |Контроллеры и маршруты
====================================


>news/views.py

                    from django.http import HttpResponse

                    def index(request):
                        # print(request)
                        return HttpResponse('<h1>Страница новостей</h1>')

Создать >newst/urls.py

                from django.urls import path

                from .views import *

                urlpatterns = [
                    path('', index),
                    path('test/', test)
                ]



>mysite/urls.py

                from django.contrib import admin
                from django.urls import path, include

                # from news.views import index, test - плохой способ


                urlpatterns = [
                    path('admin/', admin.site.urls),
                    path('news/', include('news.urls')),
                    # path('test/', test), - плохой способ
                ]



# Урок 7 | Модели
====================================

https://django.fun/docs/django/ru/3.0/topics/db/models/

id - int
title - varchar
content - text
created_at - DateTime
updated_at - DateTime
photo - Image
is-published - Boolean

from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True) # если blsnk то поле не обязательно к заполнению
    created_at = models.DateTimeField(auto_now_add=True) # добавление новости
    updated_at = models.DateTimeField(auto_now=True) # обновление новости
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)


# Урок 8 | Миграции
====================================

pip install pillow
python manage.py makemigrations
python manage.py sqlmigrate news 0001
python manage.py migrate

посмотреть в базе данных

создаем папку media в mysite/settings.py

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # создаем папку
MEDIA_URL = '/media/' # стрим url куда загружать

так же указываем в файле mysite/urls.py

    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Урок 9 | Основы работы с моделями. CRUD. Часть 1
====================================

python manage.py shell

from news.models import News

from django.db import connection
connection.queries

news1 = News(title='Новость 1', content='Контент новости 1')
news1.save()
news1.pk


news2 = News()
news2.title = 'Новость 2'
news2.content = 'Контент новости 2'
news2.save()
connection.queries

news3 = News.objects.create(title='Новость 3', content='Контент новости 3')
news3.pk
>>> news3.save()

news4 = News.objects.create(title='Новость 4', content='Контент новости 4')
news4.pk
здесь не нужно сохранять
connection.queries

News.objects.create(title='News 5', content='Content news 5')
здесь не нужно сохранять
connection.queries


# Урок 10 | Основы работы с моделями. CRUD. Часть 2
====================================
python manage.py shell
from news.models import News

News.objects.all()
[<News: News object (1)>, <News: News object (2)>, <News: News object (3)>, <News: News ob
ject (4)>, <News: News object (5)>]>

>news/models.py

        class News(models.Model):
            # . . .
            def __str__(self):
                return self.title

exit()
python manage.py shell

LOOP
from news.models import News
News.objects.all()
news = _
for item in news:
...     print(item.title, item.is_published)

CREATE
News.objects.create(title='News 5', content='News 5 content')

DELETE
News.objects.filter(title='News 5')
d = _
d.delete()

ORDER BY
News.objects.order_by('title')
News.objects.order_by('-title')

ИСКЛЮЧИТЬ С ТАКИМ TITLE
News.objects.exclude(title='Lorem ipsum')

UPDATE
news7 = News.objects.get(pk=7)
news7.title = 'News 6'
news7.save()

News.objects.filter(title='News 5')


# Урок 11 | Шаблоны
====================================
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')), # убрали путь news/
    # path('test/', test),
]

>news/views.py

                def index(request):
                    news = News.objects.all()
                    res = '<h1>Список новостей</h1>'
                    for item in news:
                        res += f'<div><p>{ item.title }</p>\n<p>{ item.content }</p>\n</div>\n<hr>\n'

                    # print(request)
                    return HttpResponse(res)

### СОЗДАЕМ ШАБЛОН


>news/urls.py убираем тестовую страницу

                from django.urls import path

                from .views import *

                urlpatterns = [
                    path('', index),
                ]


>news/views.py подключаем шаблон

    from django.shortcuts import render
    from django.http import HttpResponse

    from .models import News

    def index(request):
        news = News.objects.all()
        # render принимает request, templates название шаблона, context
        # context - это словарь где ключ 'news', news - объект новостей
        return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей'})

##### Здесь шаблон
/templates/news/index.html - по названию функции или класса во views.py

                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>{{ title }}</title>
                </head>
                <body>

                <h1>{{ title }}</h1>

                {% for item in news %}
                    <hr>
                    <div>
                        <p>{{ item.title }}</p>
                        <p>{{ item.content }}</p>
                        <p>{{ item.created_at }}</p>
                    </div>

                {% endfor %}

                </body>
                </html>

##### Дальше проверь сервер

---

##### Если контекста слишком много
>news/views.py

def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, template_name='news/index.html', context=context )


##### Изменим порядок вывода новостей     news = News.objects.order_by('-created_at')
внизу пример новые новости терерь будут сверху старые снизу
>news/views.py

def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, template_name='news/index.html', context=context )



# Урок 12 | Админка Django
====================================
новая консоль
cd mysite
python manage.py createsuperuser

Имя пользователя (leave blank to use 'admin'): admin
Адрес электронной почты: admin@mail.com
Password:
Password (again):
Введённый пароль слишком похож на имя пользователя.
Введённый пароль слишком короткий. Он должен содержать как минимум 8 символов.
Введённый пароль слишком широко распространён.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

заходим в админку наших моделей в ней нет
нужно создать

>admin.py

from django.contrib import admin

from .models import News

admin.site.register(News)

заходим и видим некрасивое отображение
>models.py
добавляем подклас для нашей рубники = Новости

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at'] # в каком порядке показывать новость

#### Добавим более информативное отображение новостей в админке
# добавим больше информации в админке новостей

                class NewsAdmin(admin.ModelAdmin):
                    list_display = ['id', 'title', 'created_at', 'updated_at', 'is_published']

                # сначала всегда основная модель потом class
                admin.site.register(News, NewsAdmin)

- посмотрим что в админке
- названия полей на английском исправим это

>apps.py

                from django.apps import AppConfig


                class NewsConfig(AppConfig):
                    name = 'news'
                    verbose_name = 'Новости'

>models.py
##### Обновим verbose_name='Наименование' и тд
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент') # если blsnk то поле не обязательно к заполнению
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации') # добавление новости
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено') # обновление новости
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

- теперь сделаем поле title ссылкой

>admin.py
list_display_links = ('id', 'title')

##### Добавим поиск по нужным полям тоже в admin
search_fields = ('title', 'content') # добаляем поис по title, content

- теперь посмотрим почему у нас попробуем добавить новость без фото(не получится)
-исправим это

>models.py

                is_published = models.BooleanField(default=True, verbose_name='Опубликовано',blank=True)

##### теперь нужно создать миграцию так как было сделано много изменений

python manage.py makemigrations
python manage.py migrate


# Урок 13 | Связи моделей
====================================
- Добавляем новую модель
>models.py

                class Category(models.Model):
                    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

                    def __str__(self):
                        return self.title

                    class Meta:
                        verbose_name = 'Категория'
                        verbose_name_plural = 'Категории'
                        ordering = ['title']




- так же добавляем внешний ключ
            class News(models.Model):
                # . . .
                category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

- null=True - как blank поле не обязательное для заполнения


python manage.py makemigrations
python manage.py migrate

##### добавляем категорию в админку

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

##### добавляем фильтры для новостей

 list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


# Урок 14 | Внешний вид шаблона подключаем Bootstrap
====================================

- Копируем стартовую страницу
>https://getbootstrap.com/docs/4.5/getting-started/introduction/#starter-template

- удаляем коментарии
- устанавливаем title и заголовок h1

                {{ title }}

- заходим в компоненты копируем navbar
>https://getbootstrap.com/docs/4.5/components/navbar/
- добавляем ссылки
- копируем карточки
>https://getbootstrap.com/docs/4.5/components/card/
- редактируем карточки

                <h1>{{ title }}</h1>
                <div class="col-md-12">
                    {% for item in news %}
                    <div class="row">
                        <div class="card mb-3">
                            <div class="card-header">
                                Категория: {{ item.category.title }}
                            </div>
                            <div class="card-body">
                                <h5 class="card-title">{{ item.title }}</h5>
                                <p class="card-text">{{ item.content }}</p>
                                <a href="#" class="btn btn-primary">Read more...</a>
                            </div>
                            <div class="card-footer text-muted">
                                {{ item.created_at | date:"Y-m-d H:i:s" }}
                            </div>
                        </div>
                    </div>
                    {% endfor %}
                </div>

- так получилось что все карточки в одну линию
- поместим их в специальный тег


# Урок 15 | Директивы, теги и фильтры. Часть 1
====================================

ВСЮ ИНФОРМАЦИЮ МОЖНО БУДЕТ ПОСМОТРЕТЬ НА САЙТЕ (djbook.ru - шаблонные теги и фильтры)[https://djbook.ru/rel3
.0/ref/templates/builtins.html]

- autoescape - отменяет экранирование

- заходим в админку новости добавляем тег <h1> в content часть
                {% autoescape off %}
                <p class="card-text">{{ item.content }}</p>
                {% endautoescape %}

- cycle - выводит аргументы в цикле, например цвета заголовков

                {% for o in some_list %}
                    <tr class="{% cycle 'row1' 'row2' %}">
                        ...
                    </tr>
                {% endfor %}

                для index.html

                <h5 class="card-title {% cycle 'text-danger' 'text-success' %}">{{ item.title }}</h5>

- filter

                {% filter force_escape|lower %}
                    This text will be HTML-escaped, and will appear in all lowercase.
                {% endfilter %}

-firstof

                {% firstof var1 var2 var3 %}

                Это равносильно:

                {% if var1 %}
                    {{ var1 }}
                {% elif var2 %}
                    {{ var2 }}
                {% elif var3 %}
                    {{ var3 }}
                {% endif %}

-for

                {% for key, value in data.items %}
                    {{ key }}: {{ value }}
                {% endfor %}


forloop.counter	            Номер текущей итерации цикла начиная с 1
forloop.counter0        	Номер текущей итерации цикла начиная с 0
forloop.revcounter	        Номер текущей итерации цикла начиная с конца с 1
forloop.revcounter0	        Номер текущей итерации цикла начиная с конца с 0
forloop.first	            True, если это первая итерация
forloop.last	            True, если это последняя итерация
forloop.parentloop	        Для вложенных циклов, это «внешний» цикл.

- reversed выводит цикл в обратном порядке

                {% for item in news reversed %}

- for ... empty

>Тег for содержит необязательную часть {% empty %}, которая будет отображена, если список пуст или не найден:

                <ul>
                {% for athlete in athlete_list %}
                    <li>{{ athlete.name }}</li>
                {% empty %}
                    <li>Sorry, no athletes in this list.</li>
                {% endfor %}
                </ul>

>Это эквивалентно, но короче, читабельней и возможно быстрее, такому коду:

                <ul>
                  {% if athlete_list %}
                    {% for athlete in athlete_list %}
                      <li>{{ athlete.name }}</li>
                    {% endfor %}
                  {% else %}
                    <li>Sorry, no athletes in this list.</li>
                  {% endif %}
                </ul>


- if

>Тег {% if %} вычисляет переменную и если она равна «true» (то есть существует, не пустая и не равна «false») выводит
содержимое блока:

{% if athlete_list %}
    Number of athletes: {{ athlete_list|length }}
{% elif athlete_in_locker_room_list %}
    Athletes should be out of the locker room soon!
{% else %}
    No athletes.
{% endif %}
>В примере выше, если athlete_list не пустой, будет отображено количество спортсменов {{ athlete_list|length }}.

>Как вы можете видеть, тег if может содержать один или несколько блоков `` {% elif %}``, так же как и блок {% else %},
который будет выведен, если все предыдущие условия не верны. Все эти блоки необязательны.

or, and

>Можно использовать and и or вместе, операция and имеет больший приоритет чем or, например:

                {% if athlete_list and coach_list or cheerleader_list %}
>будет интерпретировано как:

                if (athlete_list and coach_list) or cheerleader_list

всю информацию можно будет посмотреть на сайте (djbook.ru - шаблонные теги и фильтры)[https://djbook.ru/rel3
.0/ref/templates/builtins.html]

- now - отображает дату и время

                {% now "jS F Y H:i" %}


- regroup интересный тег посмотри на сайте

- spaceless


# Урок 16 | Директивы, теги и фильтры. Часть 2 ФИЛЬТРЫ
====================================

ВСЯ ИНФОРМАЦИЯ ПО ФИЛЬТРАМ
- add
- count
- capfirst
- center
- cut - удалить все пробелы
- date
- default - по умолцчанию
- default_if_none
- divisibleby
- escape - экранирование
- escape
- floatformat
- lower
- slice
- title
- linebreaks - оборачивает в параграф
- slugify
- timesince - показывет время прошедшее с указанной даты
- truncatechars
- truncatechars_html
- truncatewords- Обрезает строку после указанного количества слов.
- truncatewords_html


# Урок 17 | Параметры в URL-запросах
====================================

- создадим левый сайдбар для вывода категорий
- для начала получим все категории
>news.views.py
                # ...
                from .models import News, Category

                # ..

                categories = Category.objects.all()
                context = {
                        'news': news,
                        'title': 'Список новостей',
                        'category': categories,
                    }
                # ...

- добавим шаблон list group для вывода списка категорий
>https://getbootstrap.com/docs/4.5/components/list-group/

                <div class="col-md-3">
                    <div class="list-group">
                        {% for item in categories %}
                        <a href="/category/{{ item.pk }}" class="list-group-item list-group-item-action">{{ item.title }}</a>
                        {% endfor %}
                    </div>
                </div>
- у нас есть ссылка, но она не работает
- добавим для нее путь
- сначала создадим метод во views.py
>views.py

                def get_category(request, category_id):
                    news = News.objects.filter(category_id=category_id)
                    categories = Category.objects.get(pk=category_id)

>urls.py
- добавляем путь для нашей категории
urlpatterns = [
    path('', index),
    path('category/<int:category_id>', get_category)
]


# Урок 18 | Имена маршрутов
====================================

>views.py
- присваиваем имена ссылкам для удобной маршрутизации

                urlpatterns = [
                    path('', index, name='home'),
                    path('category/<int:category_id>', get_category, name='category')
                ]

>index.html
- делаем ссылки на страницы для удобной маршрутизациии

                {% url 'home' %}

- вместо этого

                <a href="/category/{{ item.pk }}" class="list-group-item list-group-item-action">{{ item.title }}</a>


-делаем это

                {% url 'category' item.pk %}


# Урок 19 | Наследование шаблонов
====================================

- создаем папку в mysite

>mysite/templates

- здесь создаем файл base.html
- КОПИРУЕМ СЮДА ВЕСЬ КОД ИЗ index.html
- назначаем title

                    <title>{% block title %}Новости со всего мира{% endblock %}</title>

- создаем панель навигации и пользуемся функцией include

                {% include 'inc\_nuv.html' %}

- создаем путь /mysite/templates/_nuv.html

>_nuv.html
                <nav class="navbar navbar-expand-lg navbar-light bg-light">
                    <a class="navbar-brand" href="{% url 'home' %}">Daily news</a>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
                            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>

                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav mr-auto">
                            <li class="nav-item"><a class="nav-link" href="{% url 'home' %}">Главная</a></li>
                            <li class="nav-item"><a class="nav-link" href="{% url 'home' %}">Добавить новость</a></li>
                        </ul>
                    </div>
                </nav>
- удаляем колонки и назначаем вместо них блоки

        {% block sidebar %}SIDEBAR{% endblock %}
        {% block content %}CONTENT{% endblock %}

> редактируем index.html

                {% extends 'base.html' %}

                {% block sidebar %}
                <div class="col-md-3">
                    <div class="list-group">
                        {% for item in categories %}
                        <a href="{% url 'category' item.pk %}" class="list-group-item list-group-item-action">{{ item.title }}</a>
                        {% endfor %}
                    </div>
                </div>
                {% endblock %}

                {% block content %}
                <div class="col-md-9">
                    {% for item in news %}
                    <div class="card mb-3">
                        <div class="card-header">
                            Категория: <a href="{% url 'category' item.category.pk %}">{{ item.category }}</a>
                        </div>
                        <div class="card-body">
                            <div class="media">
                                {% if item.photo %}
                                <img src="{{ item.photo.url }}" alt="" width="350" class="mr-3">
                                {% else %}
                                <img src="https://picsum.photos/id/1060/350/235/?blur=2" alt="" class="mr-3">
                                {% endif %}
                                <div class="media-body">
                                    <h5 class="card-title">{{ item.title }}</h5>
                                    <p class="card-text">{{ item.content|safe|linebreaks|truncatewords:50 }}</p>
                                    <a href="#" class="btn btn-primary">Read more...</a>
                                </div>
                            </div>

                        </div>
                        <div class="card-footer text-muted">
                            {{ item.created_at|date:"Y-m-d H:i:s" }}
                        </div>
                    </div>
                    {% endfor %}
                </div>
                {% endblock %}

- если попробовать зайти на сайт то ничего не получится так как не прописан путь к файлу base.html
- идем в настройки

> settings.py TEMPLATES

                'DIRS': [os.path.join(BASE_DIR, 'templates')],



# Урок 20 | Пользовательские теги шаблона
====================================

>base.html
                <div class="col-md-3">
                    {% block sidebar %}SIDEBAR{% endblock %}
                </div>
                <div class="col-md-9">
                    {% block content %}CONTENT{% endblock %}
                </div>

>index.html
- удаляем col-md-9
- создаем news/templatetags/__init__.py
- создаем news/templatetags/news_tags.py

                from django import template

                from news.models import Category

                register = template.Library()

                @register.simple_tag()
                def get_categories():
                    return Category.objects.all()

- создаем новый тег _sidebar.py
>templates/inc/_sidebar.py
-  загрушаем наш тег

                {% load news_tags %}
                <!--подключаем наш тег {% load news_tags %}, потом вызываем функцию {% get_categories as categories %}-->
                <div class="list-group">
                    {% get_categories as categories %}
                    {% for item in categories %}
                    <a href="{% url 'category' item.pk %}" class="list-group-item list-group-item-action">{{ item.title }}</a>
                    {% endfor %}
                </div>

- удаляем categories из views.py

categories = Category.objects.all()
categories = Category.objects.all()
- а так же убираем из контекста
'categories': categories,

- туперь добавим удобное нам имя для нашего тэга
> news_tags.py

                @register.simple_tag(name='get_list_categories')

- и учтем это имя в _sidebar.html

                <div class="list-group">
                    {% get_list_categories as categories %}
                    {% for item in categories %}
                    <a href="{% url 'category' item.pk %}" class="list-group-item list-group-item-action">{{ item.title }}</a>
                    {% endfor %}
                </div>

##### ИНКЛЮЖН ТЕГИ

- создадим папку для для инклюжн тегов tags
>templates/news/tags
- здесь создадим файл list_categories.html
>templates/news/tags/list_categories.html

                <!--здесь будет использоваться inclusion tag-->
                <div class="list-group">
                    {% for item in categories %}
                    <a href="{% url 'category' item.pk %}" class="list-group-item list-group-item-action">{{ item.title }}</a>
                    {% endfor %}
                </div>

- в news_tags.py создаем инклюжн тег

>news_tags.py
@register.inclusion_tag('news/tags/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {"categories": categories}

- так же можно добавлять свои аргументы

>news_tags.py

                @register.inclusion_tag('news/tags/list_categories.html')
                def show_categories(arg1='Hello', arg2='world'):
                    categories = Category.objects.all()
                    return {"categories": categories, "arg1": arg1, "arg2": arg2}
- а так же можно изменять и добавлять html шаблонах
>_sidebar.html
- добавить к show_ategories аргументы

                {% show_categories arg2='User' arg1='Hi'%}


####################################
# Урок 20 | Обратное разрешение адресов
====================================

- комментируем ненужные теги
>_sidebar.html

                {% comment %}
                <!--подключаем наш тег new_tags, потом вызываем функцию get_categories-->
                <div class="list-group">
                    {% get_list_categories as categories %}
                    {% for item in categories %}
                    <a href="{% url 'category' item.pk %}" class="list-group-item list-group-item-action">{{ item.title }}</a>
                    {% endfor %}
                </div>

                <br>

                {% endcomment %}
- здесь же убираем аргументы

{% show_categories arg2='User' arg1='Hi'%}
{% show_categories %}

- так же уберем из news_tags.py
>news_tags.py

                return {"categories": categories, "arg1": arg1, "arg2": arg2}

>list_categories.html

                {{ arg1 }} {{ arg2 }}

- получаем абсолютный путь
                from django.urls import reverse
                # ...
                class Category(models.Model):
                    def get_absolute_url(self):
                        return reverse('category', kwargs={"category_id": self.pk})
                # ...

>list_categories.html
- убираем - {% url 'category' item.pk %}


                <a href="{{ item.get_absolute_url }}" class="list-group-item list-group-item-action">{{ item.title
                }}</a>

> правим index.html

                Категория: <a href="{{ item.category.get_absolute_url }}">{{ item.category }}</a>

##### РЕАЛИЗУЕМ КНОПКУ READ MORE

>news/urls.py

                path('news/<int:news_id>/', view_news, name='view_news'),

- добавим views метод
>news/views.py

                def view_news(request, news_id):
                    news_item = News.objects.get(pk=news_id)
                    return render(request, 'news/view_news.html', {"news_item": news_item})

- создаем news/templates/news/view_news.html
>news/templates/news/view_news.html

- меняем title, item на news_item, убираем truncatewords, убираем {% for item in news %}

{% extends 'base.html' %}

                {% block title %}
                {{ news_item.title }} :: {{ block.super }}
                {% endblock %}

                {% block sidebar %}
                {% include 'inc/_sidebar.html' %}
                {% endblock %}

                {% block content %}
                <div class="card mb-3">
                        <div class="card-header">
                            Категория: <a href="{{ news_item.category.get_absolute_url }}">{{ news_item.category }}</a>
                        </div>
                        <div class="card-body">
                            <div class="media">
                                {% if item.photo %}
                                <img src="{{ news_itme.photo.url }}" alt="" width="350" class="mr-3">
                                {% else %}
                                <img src="https://picsum.photos/id/1060/350/235/?blur=2" alt="" class="mr-3">
                                {% endif %}
                                <div class="media-body">
                                    <h5 class="card-title">{{ news_item.title }}</h5>
                                    <p class="card-text">{{ news_item.content|safe|linebreaks }}</p>
                                </div>
                            </div>

                        </div>
                        <div class="card-footer text-muted">
                            {{ news_item.created_at|date:"Y-m-d H:i:s" }}
                        </div>
                    </div>

                {% endblock %}


>models.py
- добавляем абсолютный путь для новостей

class News(models.Model):
    # ...
    def get_absolute_url(self):
        return reverse('view_news', kwargs={"news_id": self.pk})
    # ...

>index.html
-меняем кнопку READ MORE

                <a href="{{ item.get_absolute_url }}" class="btn btn-primary">Read more...</a>


>category.html
-меняем кнопку READ MORE

                <a href="{{ item.get_absolute_url }}" class="btn btn-primary">Read more...</a>

- теперь рассмотрим ситуацию если страница не существует или была удалена
- если перейти на такую страницу нам покажут 500 ошибку

>views.py

from django.shortcuts import get_object_or_404

def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})

- и теперь в панели администратора у на появилась кнопка для просмотра страницы новости


# Урок 21 | Статические файлы
====================================

- скачиваем стили
> https://getbootstrap.com/docs/4.5/getting-started/download/
- Compiled CSS and JS

- создаем папку mysite/static
- рапаковываем туда стили bootstrap

> создаем mysite/static/style.css

                body {
                    background-color: #ccc;
                }
- далее прописываем путь в settings.py
>settings.py

            STATIC_URL = '/static/'
            STATIC_ROOT = os.path.join(BASE_DIR, 'static')
            STATICFILES_DIRS = {
                os.path.join(BASE_DIR, 'mysite/static'),
            }

- далее прописываем команду

                python manage.py collectstatic

- в корневой папке mysite появится папка static
>admin
>bootstrap
>css

- base.html удаляем подключение bootstrap

> base.html
- подключаем статику

                <!doctype html>
                {% load static %}
                # ...
                <link rel="stylesheet" href="{% static 'bootstrap/css/bootstrap.min.css' %}"
                <link rel="stylesheet" href="{% static 'css/style.css' %}"
- здесь же подключим js

                <script src="{% static 'bootstrap/js/bootstrap.min.js' %}"
                        integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6"
                        crossorigin="anonymous"></script>


# Урок 22 | Работа с формами. Часть 1
====================================


- Работа с формами
>https://djbook.ru/rel3.0/topics/forms/index.html
- Виджеты
>https://djbook.ru/rel3.0/ref/forms/widgets.html

##### создадим страницу добавить новость
- добавляем путь
>news/urls.py

    path('news/add-news/', add_news, name='add_news'),

- добавляем функцию
>news/views.py

            def add_news(request):
                return render(request, 'news/add_news.html')

- создаем news/templates/add_news.html
- копируем все из index.html  и правим
- очищаем поле блок контент

>add_news.html

                {% extends 'base.html' %}

                {% block title %}
                Добавление новости :: {{ block.super }}
                {% endblock %}

                {% block sidebar %}
                {% include 'inc/_sidebar.html' %}
                {% endblock %}

                {% block content %}

                <h1>Добавление новости</h1>

                {% endblock %}

- так поменяем ссылку в _nuv.html

                <li class="nav-item"><a class="nav-link" href="{% url 'add_news' %}">Добавить новость</a></li>


- создаем файл news/forms.py
>news/forms.py

                from django import forms
                from .models import Category


                class NewsForm(forms.Form):
                    titile = forms.CharField(max_length=150)
                    content = forms.CharField()
                    is_published = forms.BooleanField()
                    category = forms.ModelChoiceField(queryset=Category.objects.all())

- добавляем форму во views.py
>views.py
            def add_news(request):
                if request.method == 'POST':
                    pass
                else:
                    form = NewsForm()
                return render(request, 'news/add_news.html', {"form": form})
- добавляем форму
>add_news.html

                # ...
                <h1>Добавление новости</h1>
                <form action="{% url 'add_news' %}" method="post">
                    {% csrf token %}
                    {{ form.as_p }}
                    <button type="submit" class="btn btn-primary btn-block">Добавить новость</button>
                </form>
                # ...



# Урок 22 | Работа с формами. Часть 2
=====================================

- добавим понятные названия для нашей формы (label=)
- добавим необязательное поле(requered=)
- добавим поле по умолчанию (initial=)
- добавим выбор в выпадающем списке (empty_label=)
>forms.py

                class NewsForm(forms.Form):
                    titile = forms.CharField(max_length=150, label='Название')
                    content = forms.CharField(label='Контент', requered=False)
                    is_published = forms.BooleanField(label='Опубликовано?', initial=True)
                    category = forms.ModelChoiceField(empty_label='Выберете категорию', label='Категория',
                                                      queryset=Category.objects.all())

- переходим на сайт bootstrap, идем в documentations/components/forms
- выбираем удобную нам форму
>add_news.html
- комитим нашу форму
1)
                {% comment %}
                {{ form.as_p }}
                {% endcomment %}

- и добавляем новую
- ниже представлены два варианта для отображения и один сверху ({{ form.as_p }})
- можно использовать любой из трёх вариантов
- ЧТОБЫ ИСПОЛЬЗОВАТЬ ФОРМУ НУЖНО УБРАТЬ КОММЕНТИРОВАНИЕ

2)
- Чтобы правильно связать label указываем <label for="{{ form.title.id_for_label }}">Название: </label>
- для вывода поля input {{ form.title }}
- так выводятся ошибки валидации {{ form.title.errors }}

                    {% comment %}
                    <div class="form-group">
                        <label for="{{ form.title.id_for_label }}">Название: </label>
                        {{ form.title }}
                        <div class="invalid-feedback">
                            {{ form.title.errors }}
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="{{ form.content.id_for_label }}">Тект: </label>
                        {{ form.content }}
                        <div class="invalid-feedback">
                            {{ form.content.errors }}
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="{{ form.is_published.id_for_label }}">Опубликовано? </label>
                        {{ form.is_published }}
                        <div class="invalid-feedback">
                            {{ form.is_published.errors }}
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="{{ form.category.id_for_label }}">Категории: </label>
                        {{ form.category }}
                        <div class="invalid-feedback">
                            {{ form.category.errors }}
                        </div>
                    </div>
                    {% endcomment %}

3)
- берем каждое конкректное поле из нашей формы {% for field in form %}
- выводим label {{ field.label_tag }}
- выводим наше поле {{ field }}
- выводим ошибки:

                        <div class="invalid-feedback">
                            {{ field.errors }}
                        </div>

- третий способ ниже


                    {% comment %}
                    {% for field in form %}
                    <div class="form-group">
                        {{ field.label_tag }}
                        {{ field }}
                        <div class="invalid-feedback">
                            {{ field.errors }}
                        </div>
                    </div>
                    {% endfor %}
                    {% endcomment %}

- теперь добавим в форму виджет (widget=)
- важным элементом в котором будет form-control для красивого отображения формы
>news/forms.py

                class NewsForm(forms.Form):
                    title = forms.CharField(
                        max_length=150,
                        label='Название',
                        widget=forms.TextInput(attrs={
                            "class": "form-control"
                        }))
                    content = forms.CharField(
                        label='Текст',
                        required=False,
                        widget=forms.Textarea(attrs={
                        "class": "form-control",
                        "rows": 5,
                    }))
                    is_published = forms.BooleanField(label='Опубликовано', initial=True)
                    category = forms.ModelChoiceField(
                        queryset=Category.objects.all(),
                        label='Категории',
                        empty_label='Выберете категорию',
                        widget=forms.Select(
                            attrs={
                                "class": "form-control"
                            }))

>views.py
- проверяем форму на валидацию if form.is_valid():
- используем redirect чтобы форма не оставалась заполненной
>news/urls.py
- path('', index, name='home'),
- ПОТОМ ПОПРОБОВАТЬ лучше на страницу с отредактированной новостью

from django.shortcuts import render, get_object_or_404, redirect

                def add_news(request):
                    if request.method == 'POST':
                        form = NewsForm(request.POST)
                        if form.is_valid(): # если форма прошла валидацию
                            # print(form.cleaned_data) # если данные прошли валидацию данные попадают в словарь clean_data
                            # title = form.cleaned_data('tilte') # неудобный способ
                            # News.objects.create(title=title) # неудобный способ
                            news = News.objects.create(**form.cleaned_data) # распаковка словарей используется две звездочки (**)
                            return redirect(news)
                    else:
                        form = NewsForm()
                    return render(request, 'news/add_news.html', {"form": form})


# Урок 23 | Работа с формами. Часть 3
=====================================

- изменяем форму для более быстрого создания
- в классе meta выбираем нужные нам поля
- в виджетах создаем form-control для более удобного отображения

>forms.py

                class NewsForm(forms.ModelForm):
                    class Meta:
                        """можно использовать __all__ чтобы добавить сразу все поля, create_at и updated_at заполняются автоматически"""
                        model = News
                        # fields = '__all__'  # здесь указываются поля в нашей форме
                        # лучше описать явно поля
                        # перечисляем поля которые нам необходимы
                        fields = ['title', 'content', 'is_published', 'category']
                        widgets = {
                            'title': forms.TextInput(attrs={'class': 'form-control'}),
                            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
                            'category': forms.Select(attrs={'class': 'form-control'})
                        }

- дальше в моделях у категорий уберем null=True

                category = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, verbose_name='Категория')

- потом создадим миграцию
- py manage.py makemigrations
- и применим ее
- py manage.py migrate

- в файле views.py добавим более легкий способ сохранения формы news = form.save(

                # news = News.objects.create(**form.cleaned_data) # распаковка словарей используется две звездочки (**)
                news = form.save()



            




