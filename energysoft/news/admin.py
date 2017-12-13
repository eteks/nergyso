# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from embed_video.admin import AdminVideoMixin
# from django.shortcuts import redirect, render
# from django.shortcuts import render_to_response
from .models import News
from forms import FileFieldForm

class NewsAdmin(AdminVideoMixin, admin.ModelAdmin):
	# pass
	model = News
	form= FileFieldForm
	list_display = ('news_title','created_date','modified_date')
	list_filter = ('news_title',)

admin.site.register(News, NewsAdmin)
