# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Shoutout
from energysoft.action import export_as_csv_action
# Register your models here.

class ShoutoutAdmin(admin.ModelAdmin):
	model = Shoutout
	list_display = ('shoutout_description','created_date','shoutout_approval_status','shoutout_employee_from_id','shoutout_employee_to_id')
	list_filter = ('shoutout_approval_status','created_date',)
	search_fields = ('shoutout_description','shoutout_employee_from_id','shoutout_employee_to_id',)
	actions = [export_as_csv_action("CSV Export", fields=['id','shoutout_description','shoutout_employee_from_id','shoutout_employee_to_id','created_date'])]

	def has_add_permission(self, request):
		return False

admin.site.register(Shoutout, ShoutoutAdmin)
