from django.contrib import admin

# Register your models here.
from .models import Staff,News, Match
admin.site.register(Staff)
admin.site.register(News)
admin.site.register(Match)