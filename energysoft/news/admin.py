# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import News

# Register your models here.
class NewsAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(News, NewsAdmin)
