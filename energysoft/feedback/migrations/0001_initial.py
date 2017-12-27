# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-27 05:11
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
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_status', models.BooleanField(default=False, verbose_name='Active Status')),
                ('delete_status', models.BooleanField(default=False, verbose_name='Delete status')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Auto generated by system.')),
                ('modified_date', models.DateTimeField(auto_now_add=True, help_text='Auto generated by system.')),
                ('feedback_description', models.TextField(max_length=1000, verbose_name='Description')),
                ('feedback_queries', models.TextField(max_length=500, verbose_name='Queries')),
                ('feedback_rating_count', models.IntegerField(verbose_name='Feedback Rating')),
                ('feedback_approval_status', models.BooleanField(default=False, verbose_name='Feedback Approve By Admin')),
                ('feedback_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee', verbose_name='Employee')),
            ],
            options={
                'verbose_name': 'Feedback',
            },
        ),
    ]
