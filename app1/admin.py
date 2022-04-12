from django.contrib import admin

# Register your models here.
from .models import Staff,News
admin.site.register(Staff)
admin.site.register(News)