Set up the Django app:

Create a virtualenv

- `cd DjangoWebService`
- `virtualenv venv`

Install package 

- `venv\scripts\activate`
- `pip install django`
- `venv\scripts\deactivate`

Migration

- `cd exampleapp`
- `python manage.py migrate`

Run Test Cases
- `python manage.py test`

Run server

- `python manage.py runserver` then open URL http://127.0.0.1:8000/

