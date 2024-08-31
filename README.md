# Documentation

### Configure the Database Settings

To configure the database settings in your Django project. Open the settings.py file in your project directory and find the DATABASES section. You should see something like this:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

Suppose i want to connect database 'mysql'. So i need to change according to this...

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

This will create all the necessary tables for your Django project.
