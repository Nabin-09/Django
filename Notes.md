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

## Rendering the html file at 



