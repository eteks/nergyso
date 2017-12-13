# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from models import Employee
# from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from forms import EmployeeForm

class EmployeeAdmin(admin.ModelAdmin):
	form = EmployeeForm

admin.site.register(Employee, EmployeeAdmin)

#To unregister the user and group module since we use custom employee model
# admin.site.unregister(User)
admin.site.unregister(Group)
