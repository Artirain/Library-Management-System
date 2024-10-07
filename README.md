# Library-Management-System
**Test task "Library Management System".**


**Installing Django, DRF**
  - pip install django djangorestframework djangorestframework-simplejwt django-celery-beat


**Creating a project**
  - django-admin startproject library_project
  - cd library_project


**Creating an application**
  - python manage.py startapp library

**Adding to settings.py**

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'rest_framework_simplejwt',  
    'django_celery_beat',
    'library',        
]
```
