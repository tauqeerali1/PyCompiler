from django.contrib import admin
from .models import *
from .models import Posts

# Register your models here.

admin.site.register(Profile)
admin.site.register(Posts)