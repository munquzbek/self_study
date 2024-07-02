# This is Self Study PROJECT on Django REST API 

In this project you can study 

## Installation

python
```bash
pip install requirements.txt
```

## Usage
1. Use Postman app or similar
2. Create and fill .env as in .env.sample file
3. Run server 

```bash
python3 manage.py dumpdata fixtures/data.json
```
this code to load database with info

```url
http://127.0.0.1:8000/users/signup/
```
use this url to sign up in project
```url
http://127.0.0.1:8000/users/list/
```
list all users
```url
http://127.0.0.1:8000/users/update/1/
```
update an user with 1 id
```url
http://127.0.0.1:8000/users/delete/1/
```
delete an user with 1 id

```url
http://127.0.0.1:8000/lms/course/
```
you can change the action to GET, PUT, POST, DELETE in postman to interact with course model

```url
http://127.0.0.1:8000/lms/lesson/create/
```
```url
http://127.0.0.1:8000/lms/lesson/list/
```
```url
http://127.0.0.1:8000/lms/view/<int:pk>/
```
```url
http://127.0.0.1:8000/lms/lesson/update/<int:pk>
```
```url
http://127.0.0.1:8000/lms/lesson/delete/<int:pk>/
```

CRUD system for Lesson model

## manage survey 

```url
https://pypi.org/project/django-form-surveys/#features
```
here is a documentation about managing surveys
after creating survey you can add url of survey in lesson object in admin panel

## Thanks
