# DevLink

> Devlink is Blogging website, where user can create account and start posting & share their knowledge with people. 
> This project is built by using Django and Sqlite3 database is used for storing data.



## Demo

Please visit the [Devlink ](https://akashsabale.pythonanywhere.com/) :link:
  
## Features

- Authentication Register, Login, Logout 
- CRUD operations on post
- Upload Custom Profile Image
- Post sorting according to date posted
- Pagination


  
## Built With

#### Backend
* Django 
* Sqlite3 Database

#### Frontend
* Html Css
* Bootstrap 5

     
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`

`DEBUG`

  
## Process for Running Project 

#### create virutal env (venv)

```
python -m venv venvName
```

#### Activate venv
for path go to folder where venv is created here it is 
F:\py_django_intern\proj1\Scripts\ then write activate in last

for windows
```
F:\py_django_intern\proj1\Scripts\activate
```

#### Install project requirements
```
pip install -r requirements.txt
```

#### Make migrations and migrate to database
```
python manage.py makemigrations
python manage.py migrate

```

#### Run server
```
python manage.py runserver
```

