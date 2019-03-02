from django.contrib import admin

# Register your models here.


# this is how it shows up in our admin panel

from .models import Job

admin.site.register(Job)
