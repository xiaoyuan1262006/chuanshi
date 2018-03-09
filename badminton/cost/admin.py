from django.contrib import admin
from .models import Place,Event,Recharge

class EventAdmin(admin.ModelAdmin):
    # list_display = ['time', 'place', 'members', 'cost']
    #人员选择增加复选框
    filter_horizontal=('members',)
class RechargeAdmin(admin.ModelAdmin):
    list_display = ['time', 'member', 'recharge']

admin.site.register(Place)
admin.site.register(Event,EventAdmin)
admin.site.register(Recharge,RechargeAdmin)
