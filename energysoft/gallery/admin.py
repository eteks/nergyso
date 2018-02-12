# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Gallery
from forms import GalleryFileForm
from energysoft.action import export_as_csv_action,file_cleanup
from django.conf import settings
import os
from django.core.files.uploadedfile import SimpleUploadedFile

# Register your models here.
def handle_uploaded_file(f):
	filename, file_ext = os.path.splitext(f.name)
	suf = SimpleUploadedFile(filename + file_ext,f.read())
	Gallery().gallery_image.save(filename + file_ext, suf, save=False)
	# print gallery_image.name

class GalleryAdmin(admin.ModelAdmin):
	model = Gallery
	form= GalleryFileForm
	fields = ('gallery_title','gallery_image','gal_image',)
	readonly_fields = ['gal_image']
	list_display = ('gallery_title','created_date',)
	list_filter = ('gallery_title','created_date',)
	search_fields = ('gallery_title',)
	actions = [export_as_csv_action("CSV Export", fields=['id','gallery_title','created_date'])]
	def save_model(self,request,obj,form,change,*args, **kwargs):
		counts=len(request.FILES.getlist("gallery_image"))
		count=counts		
		# print count
		filer=''
		files = request.FILES.getlist('gallery_image')
		print files
		for x in files:
			# post_delete.connect(file_cleanup, sender=Image, dispatch_uid="gallery.image.file_cleanup")
			count=count-1
			if count==0:
				filer = filer + settings.IMAGES_ROOT + 'gallery_'+ str(x)
			else:
				filer = filer + settings.IMAGES_ROOT + 'gallery_'+ str(x) + ','
			handle_uploaded_file(x)

		# print filer
		# print self.gallery_image
		if counts!=0:
			obj.gallery_image = filer
		super(Gallery, obj).save(*args, **kwargs)

		# Gallery.objects.filter(created_date=obj.created_date,gallery_title=obj.gallery_title).update(gallery_image=filer)

admin.site.register(Gallery, GalleryAdmin)