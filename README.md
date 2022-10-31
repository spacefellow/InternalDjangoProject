## HHParseBot
A simple web application that displays crypto transaction data. It stores and serves data using Django and PostgreSQL.

### Set Up the app in Windows

> Download the code
```
$ git clone https://github.com/spacefellow/InternalDjangoProject.git
$ cd InternalDjangoProject
```

> Install modules VENV
```
$ virtualenv env
$ .\env\Scripts\activate
$ pip install -r requirements.txt
```

> Start the app
```
Set up database configuration in InternalApp/settings.py
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

At this point, the app runs at http://127.0.0.1:8000/

### Learn More
To learn Django, check out the [Django documentation](https://docs.djangoproject.com/en/4.1/)
