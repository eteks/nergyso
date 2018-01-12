# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from models import Livetelecast
from energysoft.action import export_as_csv_action
# Register your models here.


class LivetelecastAdmin(admin.ModelAdmin):
	model = Livetelecast
	list_display = ('livetelecast_url','created_date')
	list_filter = ('created_date',)
	# actions = [export_csv]
	search_fields = ('livetelecast_url',)
	actions = [export_as_csv_action("CSV Export", fields=['id','livetelecast_url','created_date'])]

admin.site.register(Livetelecast, LivetelecastAdmin)
