# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from forms import EmpFileForm
from models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
	# pass
	model = Employee
	form= EmpFileForm
	exclude = ('is_superuser','is_active','last_login','date_joined','groups','user_permissions','email',)
	list_display = ('employee_id','employee_name','employee_email','employee_mobile','employee_designation')
	list_filter = ('employee_id',)

	# def get_form(self, request, obj=None, **kwargs):
	# 	self.exclude = []
	# 	self.exclude.append('Permissions') #here!
	# 	return super(EmployeeAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(Employee, EmployeeAdmin)
