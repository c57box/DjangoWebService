Steps of setting up this app:

1. Clone repository https://github.com/c57box/DjangoWebService


2. Create a virtualenv

- `cd DjangoWebService`
- `virtualenv venv`


3. Install django

- `venv\scripts\activate`
- `pip install django`
- `venv\scripts\deactivate`


4. Migration

- `cd exampleapp`
- `python manage.py migrate`


5. Run Test Cases

- `python manage.py test`


6. Run server

- `python manage.py runserver` then open URL http://127.0.0.1:8000/

