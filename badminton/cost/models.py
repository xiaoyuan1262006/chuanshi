from django.db import models

class Place(models.Model):
    name=models.CharField('地点',max_length=50,null=True,blank=True,default=None)
    
class Event(models.Model):
    time=models.DateField('时间',null=True,blank=True,default=None)
    place=models.ForeignKey(verbose_name='地点',null=True,blank=True,default=None)
    members=models.ManyToManyField(ManyToManyField,verbose_name='参与人',null=True,blank=True,default=None)
    cost=models.DecimalField('消费金额',max_digits=5, decimal_places=2,null=True,blank=True,default=None)

