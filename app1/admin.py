from django.contrib import admin
from  embed_video.admin  import  AdminVideoMixin
# Register your models here.
from .models import Staff,Expenses,Revenue, Report, Streaming
admin.site.register(Staff)
admin.site.register(Expenses)
admin.site.register(Revenue)
admin.site.register(Report)

class  StreamingAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(Streaming, StreamingAdmin)