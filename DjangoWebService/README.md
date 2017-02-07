Steps of setting up this app:

Clone repository https://github.com/c57box/DjangoWebService


Create a virtualenv

- `cd DjangoWebService`
- `virtualenv venv`


Install django

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

