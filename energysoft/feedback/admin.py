# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Feedback
# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
	model = Feedback
	list_display = ('feedback_description','feedback_queries','feedback_category','created_date','feedback_approval_status')
	list_filter = ('feedback_category','feedback_approval_status','created_date',)
	# updated by kalai
	readonly_fields = ['feedback_category_id']
	def has_add_permission(self, request):
		return False
admin.site.register(Feedback, FeedbackAdmin)
