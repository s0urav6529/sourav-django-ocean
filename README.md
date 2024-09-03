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

### Django Create Project

    django-admin startproject my_first_project

Django creates a **my_first_project** folder on my computer, with this content:

    my_tennis_club
        manage.py
        my_tennis_club/
            __init__.py
            asgi.py
            settings.py
            urls.py
            wsgi.py

Here, we have a manage.py file.Which is use for run this project in the webserver.

#### Run the Django Project

Navigate to the /**my_first_project** folder and execute this command in the command prompt:

    py manage.py runserver

### Django Create App

You should be in the **project folder** to make an app for the project.Then run the command.

    py manage.py startapp <app_name(suppose)> myapp

Django creates a folder named **myapp** in my project, with this content:

    my_first_project
        manage.py
        my_first_project/
        myapp/
            migrations/
                __init__.py
            __init__.py
            admin.py
            apps.py
            models.py
            tests.py
            views.py

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
