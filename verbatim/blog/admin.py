
# Register your models here.

from django.contrib import admin
from .models import Post 

# add models to admin site
admin.site.register(Post)