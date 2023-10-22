# Project setup

### Create a virtual environment

`python -m venv env`  
`source env/bin/activate` // for linux
`env\Scripts\activate` // for windows

### Install dependencies

`pip install -r requirements.txt`

### Sync your database

`python manage.py migrate`

### Create an initial user

`python manage.py createsuperuser --email admin@example.com --username admin`

### run project server
`python manage.py runserver`
