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
    members=models.ManyToManyField(User,verbose_name='参与人',null=True,blank=True,default=None)
    cost=models.DecimalField('消费金额',max_digits=5, decimal_places=2,null=True,blank=True,default=None)

    def __str__(self):
        return '%s %s' % (self.time,self.place)

    class Meta:
        ordering = ('-time',)
        verbose_name = '活动'
        verbose_name_plural = verbose_name

class Recharge(models.Model):
    time = models.DateField(verbose_name='时间', null=True, blank=True, default=None)
    member = models.ForeignKey(User, verbose_name='人员', null=True, blank=True, default=None)
    recharge = models.DecimalField(verbose_name='充值金额',max_digits=5, decimal_places=2, null=True, blank=True, default=100.00)

    def __str__(self):
        return '%s %s' % (self.time,self.member)

    class Meta:
        ordering = ('-time',)
        verbose_name = '充值'
        verbose_name_plural = verbose_name

class Recharge_and_cost(models.Model):
    event=models.ForeignKey(Event,verbose_name='事件',null=True,blank=True,default=None)
    member=models.ForeignKey(User,verbose_name='人员',null=True,blank=True,default=None)
    cost=models.DecimalField(verbose_name='消费金额',max_digits=5,decimal_places=2,null=True,blank=True,default=0.00)
    recharge=models.ForeignKey(Recharge,verbose_name='充值金额',null=True,blank=True,default=None)

    def __str__(self):
        return '%s %s %s %s' % (self.event,self.member,self.cost,self.recharge)

    class Meta:
        ordering = ('-event',)
        verbose_name = '充值及消费记录'
        verbose_name_plural = verbose_name


