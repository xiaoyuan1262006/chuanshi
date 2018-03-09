from django.contrib import admin
from .models import Place,Event,Recharge,Recharge_and_cost

class EventAdmin(admin.ModelAdmin):
    list_display = ['time', 'place', 'iteMembers', 'cost']
    filter_horizontal=('members',)
    list_filter=('place', 'cost' )

    def save_model(self, request, obj, form, change):
        id=obj.id

        if change:
            for recharge_and_cost in obj.event_costs.all():
                recharge_and_cost.delete()
        else:
            obj.save()
        for member in form.cleaned_data['members']:
            Recharge_and_cost.objects.create(
                event=obj,
                member=member,
                cost=form.cleaned_data['cost']/form.cleaned_data['members'].count()
            )
        super().save_model(request, obj, form, change)

class RechargeAdmin(admin.ModelAdmin):
    list_display = ['time', 'member', 'recharge']

class Recharge_and_costAdmin(admin.ModelAdmin):
    list_display = ['event', 'member', 'cost']

admin.site.register(Place)
admin.site.register(Event,EventAdmin)
admin.site.register(Recharge,RechargeAdmin)
admin.site.register(Recharge_and_cost,Recharge_and_costAdmin)
