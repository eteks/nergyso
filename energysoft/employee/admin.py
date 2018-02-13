# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from forms import EmpFileForm
from models import Employee,User
from energysoft.action import export_as_csv_action
# from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# class UserAdmin(admin.ModelAdmin):
# 	# pass
# 	model = User
# 	#updated by kalai
# 	# exclude = ('password','is_superuser','is_active','last_login','date_joined','groups','user_permissions','employee_aadhar_id','is_staff','active_status','delete_status','employee_device_id')
# 	exclude = ('groups','user_permissions')
# 	# fields = ('username','first_name','last_name','email','password','last_login','date_joined','is_active','is_staff','is_superuser',)
# admin.site.unregister(User)	
# admin.site.register(User, UserAdmin)

class EmployeeAdmin(admin.ModelAdmin):
	# pass
	model = Employee
	form= EmpFileForm
	#updated by kalai

	# exclude = ('password','is_superuser','is_active','last_login','date_joined','groups','user_permissions','employee_aadhar_id','is_staff','active_status','delete_status','employee_device_id')
	# exclude = ('password','first_name','last_name','is_superuser','is_active','last_login','date_joined','groups','user_permissions','email','employee_aadhar_id','is_staff','employee_device_id')
	fields = ('username','first_name','last_name','email','employee_id','employee_name','employee_dob','employee_mobile','employee_doj','employee_department','employee_designation','employee_photo','gal_image','employee_bloodgroup','employee_address','employee_experience_in_years','active_status','delete_status')
	readonly_fields = ['gal_image']
	list_display = ('employee_id','employee_name','employee_mobile','employee_designation')
	list_filter = ('employee_id',)
	search_fields = ('employee_id','employee_name','employee_mobile','employee_designation',)
	actions = [export_as_csv_action("CSV Export", fields=['employee_id','employee_name','employee_dob ','employee_mobile','employee_doj','employee_designation','employee_bloodgroup','employee_address','employee_experience_in_years','employee_device_id','employee_department_id'])]
	#updated by kalai
	# readonly_fields = ['employee_device_id',]

admin.site.register(Employee, EmployeeAdmin)

#To unregister the user and group module since we use custom employee model
# admin.site.unregister(User)
admin.site.unregister(Group)