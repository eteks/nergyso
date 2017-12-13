# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Shoutout
# Register your models here.

class ShoutoutAdmin(admin.ModelAdmin):
	model = Shoutout
	list_display = ('shoutout_description','created_date','shoutout_approval_status')
	list_filter = ('shoutout_approval_status','created_date',)

	def has_add_permission(self, request):
		return False

admin.site.register(Shoutout, ShoutoutAdmin)
