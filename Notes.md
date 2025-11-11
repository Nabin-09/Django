# Django

## Learn About Virtual Environment

``` django-admin startproject <projectname> ```
This happens further on we make apps 

### Steps to run a server : 

```
$ django-admin startproject course
$ cd course
$ py manage.py runserver
```

### settings.py
 
- has installed apps
- middlewares
- templates
- databases

### urls.py 

- routing (logic written in views.py and model.py has db models)

## Templates and Errors 

### Basics Architecture :

![architecture](https://github.com/Nabin-09/Django/blob/main/images/architecture.png?raw=1)

### views.py 

- To send a response we would : 

```py
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello Dunia!')

def about(request):
    return HttpResponse('This is about page')

def contact(request):
    return HttpResponse('What request would you like to make ?')

```

### urls.py to handle and route requests

```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home , name = 'home'),
    path('about/' , views.about , name = 'about'),
    path('contact/' , views.contact , name='contact')
]
```

### Templates

Create folder <templates> and <static> at root dir on the same level of manage.py.<br>

## Rendering the html file

```python
from django.shortcuts import render
def home(request):
    #return HttpResponse('Hello Dunia!')
    return render(request , 'index.html')
```
 > How will it know where is the template 

### Try linking a CSS file :

>Linking in HTML wont do the task.<br>
**Templating Engines** are the way to do so

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nabin Sharma-Django</title>
    <link rel="stylesheet" href="{% static 'style.css' %}">
</head>
<body>
    <h1>Nabin is learning Django</h1>
</body>
</html>
```
Even after the above code , style woudn't be visible

```python
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```
this is how static files are loaded 

## Jinja and Django apps :

Command to createapp

```
 python manage.py startapp <appname>
```
We create templates as we used to but where will the url be hit , we dont have a urls.py<br>
that is where this is come into play.

![arch-2](https://github.com/Nabin-09/Django/blob/main/images/arch-2.png?raw=1)

### Including app in my main-app(course) : 
```
path('nabin/' , include('nabin.urls'))
```

### How to handle path in nabin/course

```python

from django.urls import path
from . import views


 
urlpatterns = [
   path('' , views.all_items , name='all_items')
]

```