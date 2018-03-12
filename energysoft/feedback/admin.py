# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from energysoft.action import export_as_csv_action
from models import Feedback
# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
	model = Feedback
	list_display = ('feedback_description','feedback_queries','feedback_employee_id','created_date','feedback_approval_status')
	list_filter = ('feedback_approval_status','created_date',)
	search_fields = ('feedback_description','feedback_queries','feedback_employee_id',)
	actions = [export_as_csv_action("CSV Export", fields=['id','feedback_description','feedback_queries','feedback_employee_id','created_date'])]
	# readonly_fields = ['feedback_category_id']
	def has_add_permission(self, request):
		return False
admin.site.register(Feedback, FeedbackAdmin)
