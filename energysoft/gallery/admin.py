# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Gallery
# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
	pass

admin.site.register(Gallery, GalleryAdmin)