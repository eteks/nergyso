# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Gallery
from forms import GalleryFileForm
from energysoft.action import export_as_csv_action

# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
	model = Gallery
	form= GalleryFileForm
	search_fields = ('gallery_title',)
	actions = [export_as_csv_action("CSV Export", fields=['id','gallery_title','created_date'])]

admin.site.register(Gallery, GalleryAdmin)