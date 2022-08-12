# Register your models here.

from django.contrib import admin
from .models import * 

#your model will be registered right here
admin.site.register(forum)
admin.site.register(Discussion)

# py manage.py makemigrations
# py manage.py migrate
# py manage.py createsuperuser