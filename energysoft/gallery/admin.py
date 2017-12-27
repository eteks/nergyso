# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Gallery
from forms import GalleryFileForm
# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
	model = Gallery
	form= GalleryFileForm
	list_display = ('gallery_title','created_date','gal_image')
	list_filter = ('gallery_title','created_date')

admin.site.register(Gallery, GalleryAdmin)