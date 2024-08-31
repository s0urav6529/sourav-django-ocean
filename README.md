# Documentation

### Virtual Environment

It is suggested to have a dedicated virtual environment for each Django project, and one way to manage a virtual environment is venv, which is included in Python.

Windows:

    py -m venv myworld

Unix/MacOS:

    python -m venv myworld

Then you have to activate the environment, by typing this command:

Windows:

    myworld\Scripts\activate.bat

Unix/MacOS:

    source myworld/bin/activate

you can deactivate your virtual environment by typing the following command into your terminal or command line:

    deactivate

### Install Django

After activation of 'venv' then need to install Django.Django is installed using pip, with this command:

Windows:

    (myworld) C:\Users\Your Name> py -m pip install Django

Unix/MacOS:

    (myworld) ... $ python -m pip install Django

#### Can check if Django is installed by asking for its version number like this:

    (myworld) C:\Users\Your Name>django-admin --version

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
            'NAME': 'database_name',
            'USER': 'database_user',
            'PASSWORD': 'database_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

Here, replace database_name, database_user, and database_password with your own values.

### Create Database Tables

After configuring the database settings, you need to create the database tables.

In linux

    python manage.py migrate

or windows

    py manage.py migrate

This will create all the necessary default tables for your Django project.

#### create a table

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
