# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Livetelecast
# Register your models here.

class LivetelecastAdmin(admin.ModelAdmin):
	model = Livetelecast
	list_display = ('livetelecast_url','created_date')
	list_filter = ('livetelecast_url','created_date',)

admin.site.register(Livetelecast, LivetelecastAdmin)
