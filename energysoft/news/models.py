from __future__ import unicode_literals

from django.db import models
from master.models import AbstractDefault
from django.conf import settings
from forms import FileFieldForm
from django.core.exceptions import ValidationError

# print current_site_url()

def update_image(instance, filename):
	image_path = settings.IMAGES_ROOT
	image_root=image_path+"news_"+filename
	return image_root

def update_video(instance, filename):
	video_path = settings.VIDEOS_ROOT	   
	video_root=video_path+"news_"+filename
	return video_root

def update_file(instance, filename):
	file_path = settings.DOCUMENT_ROOT
	file_root=file_path+"news_"+filename
	return file_root

class News(AbstractDefault):
	news_title = models.CharField(verbose_name = 'Title', max_length = 255)
	news_description = models.TextField(verbose_name = 'Description', max_length = 1000)
	news_image = models.ImageField(verbose_name = 'Images',upload_to = update_image)
	news_video = models.FileField(verbose_name = 'Video',upload_to = update_video) 
	news_document = models.FileField(verbose_name = 'Document',upload_to = update_file)

	def __str__(self):
		return self.news_title

	def admin_image(self):
		return '<img src="'+settings.SITE_URL+'%s" width="100px"/>' % self.news_image
    	admin_image.allow_tags = True
    	admin_image.short_description = 'News Image'

	class Meta:
		verbose_name = "New"
		verbose_name_plural = "News"
		ordering = ['id']