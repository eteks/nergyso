# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Feedback
# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
	pass

admin.site.register(Feedback, FeedbackAdmin)
