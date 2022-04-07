from django.contrib import admin

# Register your models here.
from .models import Staff,Expenses,Revenue, Report
admin.site.register(Staff)
admin.site.register(Expenses)
admin.site.register(Revenue)
admin.site.register(Report)