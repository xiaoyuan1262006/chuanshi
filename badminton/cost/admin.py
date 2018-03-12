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
    list_filter = ('member',)
    def save_model(self, request, obj, form, change):
        id=obj.id

        if change:
            for recharge_and_cost in obj.recharge_recharges.all():
                recharge_and_cost.delete()
        else:
            obj.save()

        Recharge_and_cost.objects.create(
            recharge=obj,
            member=obj.member,
            # amount=form.cleaned_data['recharge']
            )
        super().save_model(request, obj, form, change)

class RechargeAndCostEventFilter(admin.SimpleListFilter):
    title='事件类型'
    parameter_name=''
    
    def lookups(self, request, model_admin):
        return (
            ('event', '活动'),
            ('recharge', '充值'),
        )
        
    def queryset(self, request, queryset):
        if self.value()=='event':
            return queryset.filter(event__isnull=False)
        if self.value()=='recharge':
            return queryset.filter(recharge__isnull=False)
            
class Recharge_and_costAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'member', 'cost','time','place','amount']
    list_filter = ('member',RechargeAndCostEventFilter)
    list_display_links=None
    actions=None
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(member=request.user)

admin.site.register(Place)
admin.site.register(Event,EventAdmin)
admin.site.register(Recharge,RechargeAdmin)
admin.site.register(Recharge_and_cost,Recharge_and_costAdmin)
