from django.contrib import admin
from  embed_video.admin  import  AdminVideoMixin
# Register your models here.
from .models import Staff,Expenses,Revenue, Report, Streaming, Merchandise, Match
admin.site.register(Staff)
admin.site.register(Expenses)
admin.site.register(Revenue)
admin.site.register(Report)
admin.site.register(Merchandise)
admin.site.register(Match)

class  StreamingAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(Streaming, StreamingAdmin)