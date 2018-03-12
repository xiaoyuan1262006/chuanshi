from django.db import models
from django.contrib.auth.models import User

class Place(models.Model):
    name=models.CharField('地点',max_length=50,null=True,blank=True,default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '地点'
        verbose_name_plural = verbose_name

class Event(models.Model):
    time=models.DateField('时间',null=True,blank=True,default=None)
    place=models.ForeignKey(Place,verbose_name='地点',null=True,blank=True,default=None)
    members=models.ManyToManyField(User,verbose_name='参与人',blank=True,default=None)
    cost=models.DecimalField('消费金额',max_digits=5, decimal_places=2,null=True,blank=True,default=None)

    def __str__(self):
        return '%s %s'  % (self.time,self.place)

    def iteMembers(self):
        stringname = ''
        for person in self.members.all():
            stringname += person.username+" "
        return  stringname

    iteMembers.short_description='参与人'

    class Meta:
        ordering = ('time',)
        verbose_name = '活动'
        verbose_name_plural = verbose_name

class Recharge(models.Model):
    time = models.DateField(verbose_name='时间', null=True, blank=True, default=None)
    member = models.ForeignKey(User, verbose_name='人员', null=True, blank=True, default=None)
    recharge = models.DecimalField(verbose_name='充值金额',max_digits=5, decimal_places=2, null=True, blank=True, default=100.00)

    def __str__(self):
        return '%s' % self.time

    class Meta:
        ordering = ('-time',)
        verbose_name = '充值'
        verbose_name_plural = verbose_name

class Recharge_and_cost(models.Model):
    event=models.ForeignKey(Event,verbose_name='事件',null=True,blank=True,default=None,related_name='event_costs')
    member=models.ForeignKey(User,verbose_name='人员',null=True,blank=True,default=None)
    cost=models.DecimalField(verbose_name='消费金额',max_digits=5,decimal_places=2,null=True,blank=True,default=0.00)
    recharge=models.ForeignKey(Recharge,verbose_name='充值',null=True,blank=True,default=None,related_name='recharge_recharges')
    # amount = models.DecimalField(verbose_name='充值金额',max_digits=5, decimal_places=2, null=True, blank=True, default=0.00)

    def __str__(self):
        return '%s %s %s %s' % (self.event,self.member,self.cost,self.recharge)

    class Meta:
        ordering = ('-event','recharge')
        verbose_name = '充值及消费记录'
        verbose_name_plural = verbose_name

    def amount(self):
        if self.recharge:
            return self.recharge.recharge
        else:
            return 0
    amount.short_description='充值金额'

    def time(self):
        if self.recharge:
            return self.recharge.time
        else:
            return self.event.time
    time.short_description='发生时间'
    
    def place(self):
        if self.event:
            return self.event.place
        else:
            return ''
    place.short_description='发生地点'
    
    def event_name(self):
        if self.event:
            return '活动'
        else:
            return '充值'
    event_name.short_description='事件'