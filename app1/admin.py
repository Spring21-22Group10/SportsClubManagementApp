from django.contrib import admin
from  embed_video.admin  import  AdminVideoMixin
# Register your models here.
from .models import Staff,Expenses,Revenue, Match,Merchandise, Report
admin.site.register(Staff)
admin.site.register(Expenses)
admin.site.register(Revenue)
admin.site.register(Report)
admin.site.register(Merchandise)

class  MatchAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(Match, MatchAdmin)