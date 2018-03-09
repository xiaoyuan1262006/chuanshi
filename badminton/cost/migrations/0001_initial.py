# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-08 15:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(blank=True, default=None, null=True, verbose_name='时间')),
                ('cost', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True, verbose_name='消费金额')),
                ('members', models.ManyToManyField(blank=True, default=None, null=True, to=settings.AUTH_USER_MODEL, verbose_name='参与人')),
            ],
            options={
                'verbose_name_plural': '活动',
                'verbose_name': '活动',
                'ordering': ('-time',),
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='地点')),
            ],
            options={
                'verbose_name_plural': '地点',
                'verbose_name': '地点',
            },
        ),
        migrations.CreateModel(
            name='Recharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(blank=True, default=None, null=True, verbose_name='时间')),
                ('recharge', models.DecimalField(blank=True, decimal_places=2, default=100.0, max_digits=5, null=True, verbose_name='充值金额')),
                ('member', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='人员')),
            ],
            options={
                'verbose_name_plural': '充值',
                'verbose_name': '充值',
                'ordering': ('-time',),
            },
        ),
        migrations.CreateModel(
            name='Recharge_and_cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True, verbose_name='消费金额')),
                ('event', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cost.Event', verbose_name='事件')),
                ('member', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='人员')),
                ('recharge', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cost.Recharge', verbose_name='充值金额')),
            ],
            options={
                'verbose_name_plural': '充值及消费记录',
                'verbose_name': '充值及消费记录',
                'ordering': ('-event',),
            },
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cost.Place', verbose_name='地点'),
        ),
    ]
