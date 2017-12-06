# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Events

# Register your models here.
class EventsAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(Events, EventsAdmin)
