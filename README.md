# Documentation

### Work flow of Django

Django basically follows **MVT** structure.

![Screenshot 2024-09-03 135709](https://github.com/user-attachments/assets/2a5770cd-1bf0-4851-80fb-d32c937593ce)

![Screenshot 2024-09-03 140137](https://github.com/user-attachments/assets/688cd941-94a2-4497-8403-884a64018bf5)

### Virtual Environment

It is suggested to have a dedicated virtual environment for each Django project, and one way to manage a virtual environment is venv, which is included in Python.It's better to have a separate **venv** for every particular project.

Windows:

    py -m venv myworld

Unix/MacOS:

    python -m venv myworld

Then you have to activate the environment, by typing this command:

Windows:

    myworld\Scripts\activate

Unix/MacOS:

    source myworld/bin/activate

you can deactivate your virtual environment by typing the following command into your terminal or command line:

    deactivate

### Install Django

After activation of 'venv' then need to install Django.Django is installed using pip, with this command:

Windows:

    py -m pip install Django

Unix/MacOS:

    python -m pip install Django

#### Can check if Django is installed by asking for its version number like this:

    django-admin --version

#### If problem with mariadb

    pip install 'django<4'

### Directory Hierarchy

A well-organized project structure typically follows this hierarchy:

![Screenshot 2024-09-05 104124](https://github.com/user-attachments/assets/e5d6a5e4-3757-4c79-b770-73f266e7c178)

#### project_name:

The root directory of your project.

#### project_name/project_name:

This inner directory holds core project settings and configuration.

#### app1, app2:

These are the individual apps you create within the project.

#### static:

Houses static files like CSS, JavaScript, and images.

#### media:

Stores user-uploaded files.

#### templates:

Contains HTML templates.

### Django Create Project

    django-admin startproject my_project

Django creates a **my_project** folder on my computer, with this content:

![Screenshot 2024-09-05 103824](https://github.com/user-attachments/assets/38654598-2f89-4af6-8a46-957bc37f828a)

Here, we have a manage.py file.Which is use for run this project in the webserver.

#### Run the Django Project

Navigate to the /**my_project** folder and execute this command in the command prompt:

    py manage.py runserver

### Django Create App

You should be in the **project folder** to make an app for the project.Then run the command.

    py manage.py startapp teacher

Django creates a folder named **teacher** in my project, with this content:

    my_project
        manage.py
        my_project/
        teacher/
            migrations/
                __init__.py
            __init__.py
            admin.py
            apps.py
            models.py
            tests.py
            views.py

After creating the **teacher** we need to register this app in main **project**. So that the project can recognize the app easily.

For this we need to go **project_innner_folder/setting.py** then register in the **INSTALLED_APPS** list.

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        **created external apps**
        'teacher',
        'student',
    ]

### Create view in every app

Now go to the **teacher/views.py** file & define functions

    def course(request) :
        return HttpResponse('Welcome to teacher course that conducted')

    def course2(request) :
        return HttpResponse('Welcome to teacher course2 that conducted')

Again go to **student/views.py** file & define functions

    def subject(request) :
        return HttpResponse('Welcome to student subject that a student complete in class')

    def subject2(request) :
        return HttpResponse('Welcome to student subject2 that a student complete in class')

### Create url to use views from apps

Now go to **my_project/url.py** file register those views path

#### Type 1 : rename views

    from teacher import views as teacher_views
    from student import views as student_views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('teacher/', teacher_views.course),
        path('teacher2/', teacher_views.course2),
        path('student/', student_views.subject),
        path('student2/', student_views.subject2),
    ]

#### Type 2 : import directly functions

    from teacher.views import course, course2
    from student.views import subject, student2

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('teacher/', course),
        path('teacher2/', course2),
        path('student/', subject),
        path('student2/', subject2),
    ]

This looks so messy. so for ignoring this extrame code writting condition, we nedd to create a **urls.py** file in every app. Then just link the file in the main project **urls.py**

In **teacher.urls.py** file

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.course),
        path('2/', views.course2),
    ]

In **student.urls.py** file

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.subject),
        path('2/', views.subject2),
    ]

In **my_project.urls.py** file

    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('teacher/', include('teacher.urls')),
        path('student/', include('student.urls')),
    ]

### Templates

Template folder always be in outer folder of **my_project/templates/**. After creating this folder, we need to register this folder in the inner folder of **my_project/settings.py**. Then write this below **BASE_DIR**

    import os

    TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')

After create **TEMPLATE_DIR** register in TEMPLATES list.

    TEMPLATES = [
        {
            .....
            'DIRS': [TEMPLATE_DIR],
            'APP_DIRS': True,
            .....
        },
    ]

### Render templates in view

After complete register **TEMPLATE_DIR**. Create a folder **teacher** & a html page name **course**.After creating, we need to go in view of app & render.

    def machine(request) :
        return render(request,'teacher/course.html')

### Django Template Language

In html file, **dictionary** keys of views file works as **variables**

    def course(request):
        name = "History"
        context = {'name': name}
        return render(request, 'teacher/course.html', context)

Now we can use this **name** key of dictonary key as variable in html file.

#### Variables

It associated with a context can be accessed by **{{}}**

    {{ variable }}

#### Filter

Django Template Engine provides filters which are used to transform the values of variables and tag arguments.

    {{ variable | filter }}

Major Template Filters in Django link.

    https://www.geeksforgeeks.org/django-template-filters/

#### Tags

In Django templates,using tags you can perform programming logic like executing **if** statements and **loops**.

    {%  %}

For more details

    https://www.w3schools.com/django/django_template_tags.php

#### Static Folder

Django use static folder for (css,js & image etc). So similarly as template folder, need to crate a folder static folder in outer **my_project/static**.
After that we need to register this folder in the **settings.py** file.

    STATIC_DIR = os.path.join(BASE_DIR,'static')

After create **STATIC_DIR** register in **STATICFILES_DIRS** list.

    STATIC_URL = 'static/'
    STATICFILES_DIRS = [ STATIC_DIR, ]

#### How to use this static folder contents

In html file we need to load the static, after that in head we need to link particular static file

    <!DOCTYPE html>
    {% load static %}   //load the static
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <title></title>
        <meta name="description" content="" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="stylesheet" href="{% static 'css/style.css' %}" />   //link particular css file
    </head>
    <body>

        <h1>Hello, Deep learning</h1>

        <script src="" async defer></script>
    </body>
    </html>

#### Load any image from static folder

    <body>
        <img src = "{% static 'images/image_name.jpg' %}">
    </body>

### Mastering in Template

### URL namming

    urlpattern = [
        path('blog-all/', views.blog_all, name = 'blg_all'),
        path('blog-details/', views.blog_details, name = 'blg_details'),
        ..........
    ]

In href

    href = {% url = 'blg_all' %}
    href = {% url = 'blg_details' %}

### ORM (Object Relational Mapper) & it's work

![Screenshot 2024-09-05 110423](https://github.com/user-attachments/assets/519ef3ef-2dba-4475-b532-9c293ee76157)

It basically works as a converter, where we just use the django model to CRUD the data from database. ORM converts the class into sql of database & gives us results.

![Screenshot 2024-09-05 110611](https://github.com/user-attachments/assets/7aa57660-3f73-493f-a981-3157433eddf6)

### Configure the Database Settings

To configure the database settings in your Django project. Open the settings.py file in your project directory and find the DATABASES section. You should see something like this:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

Suppose i want to connect database **mysql**. So i need to change according to this...

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '<database_name>',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

Here, replace database_name, database_user, and database_password with your own values.

### Create Database Tables/Models

For creating a database table/model in django follow the rules...

    from django.db import models

    class Person(models.Model):
        name = models.CharField(max_length=100)
        age = models.IntegerField()
        phone = models.IntegerField(null=True)
        joined_date = models.DateField(null=True)

        def __str__(self):
            return self.name

The **str** method is used to display the name of the person instead of its object ID.

To use this model, you need to create a new migration:

    py manage.py makemigrations

This will generate a new migration file that contains the changes made to your models. You can then apply the migration using:

    py manage.py migrate
