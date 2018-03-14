# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from energysoft.action import export_as_csv_action
# from django.shortcuts import redirect, render
# from django.shortcuts import render_to_response
from .models import News
from forms import FileFieldForm
from django.conf import settings
import os
from django.core.files.uploadedfile import SimpleUploadedFile
from master.models import Notification
def handle_uploaded_file(f):
    filename, file_ext = os.path.splitext(f.name)
    suf = SimpleUploadedFile(filename + file_ext,f.read())
    News().news_image.save(filename + file_ext, suf, save=False)

class NewsAdmin(AdminVideoMixin, admin.ModelAdmin):
	# pass
	model = News
	form= FileFieldForm
	fields = ('active_status','delete_status','news_title','news_description','news_image','gal_image',)
	readonly_fields = ['gal_image']
	list_display = ('news_title','created_date','modified_date')
	list_filter = ('news_title',)
	search_fields = ('news_title',)
	actions = [export_as_csv_action("CSV Export", fields=['id','news_title','news_description','created_date'])]

	def save_model(self,request,obj,form,change,*args,**kwargs):
		counts=len(request.FILES.getlist("news_image"))
		count=counts 
        # print count
		filer=''
		files = request.FILES.getlist('news_image')
		for x in files:
			count=count-1
			if count==0:
				filer = filer + settings.IMAGES_ROOT + 'news_'+ str(x)
			else:
				filer = filer + settings.IMAGES_ROOT + 'news_'+ str(x) + ','
			handle_uploaded_file(x)
		if counts!=0:	
			obj.news_image = filer
		super(News, obj).save(*args,**kwargs)


	def delete_model(self,request,obj,*args,**kwargs):
		Notification.objects.filter(notification_cateogry_id=obj.id,notification_cateogry__icontains="news").delete()

admin.site.register(News, NewsAdmin)
