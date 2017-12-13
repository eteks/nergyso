# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-11 08:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_status', models.BooleanField(default=False, verbose_name='Active Status')),
                ('delete_status', models.BooleanField(default=False, verbose_name='Delete status')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Auto generated by system.')),
                ('modified_date', models.DateTimeField(auto_now_add=True, help_text='Auto generated by system.')),
                ('department_name', models.CharField(max_length=50, verbose_name='Department Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_cateogry', models.IntegerField(choices=[(b'events', b'Events'), (b'news', b'News'), (b'shoutout', b'Shoutout')], verbose_name='Notification Category')),
                ('notification_cateogry_id', models.IntegerField(verbose_name='Notification Category Id')),
                ('notification_delivery_status', models.BooleanField(default=False, verbose_name='Notification Delivery Status')),
                ('notification_read_status', models.BooleanField(default=False, verbose_name='Notification Read Status')),
                ('notification_created_date', models.DateTimeField(auto_now_add=True, help_text='Auto generated by system.')),
                ('notification_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee', verbose_name='Employee')),
            ],
        ),
    ]
