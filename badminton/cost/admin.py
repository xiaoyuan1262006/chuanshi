from django.contrib import admin
from .models import Place,Event,Recharge

class EventAdmin(admin.ModelAdmin):
    #人员选择增加复选框
    filter_horizontal=('members',)

admin.site.register(Place)
admin.site.register(Event,EventAdmin)
admin.site.register(Recharge)