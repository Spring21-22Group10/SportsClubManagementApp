from django.contrib import admin
from  embed_video.admin  import  AdminVideoMixin
# Register your models here.
from .models import Staff,Expenses,Revenue, Match,Merchandise, Report, Fan
admin.site.register(Staff)
admin.site.register(Expenses)
admin.site.register(Revenue)
admin.site.register(Report)
admin.site.register(Merchandise)
admin.site.register(Fan)

class  MatchAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(Match, MatchAdmin)