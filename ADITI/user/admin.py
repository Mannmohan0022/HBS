from django.contrib import admin
from .models import CustomUser, Userdetails
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Userdetails)