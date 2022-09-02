from .base import *      
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'proyectoinfo',
        'USER': 'test', 
        'PASSWORD':#'matu22',
        'HOST':'localhost',
        'PORT':'3306',
    }
}