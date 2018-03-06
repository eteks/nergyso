# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Department,Notification,CEOMessage
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
	pass

class NotificationAdmin(admin.ModelAdmin):
	pass

class CEOMessageAdmin(admin.ModelAdmin):
	pass

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(CEOMessage, CEOMessageAdmin)
