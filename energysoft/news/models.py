# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import string
import os
from django.db import models
from embed_video.fields import EmbedVideoField
from master.models import AbstractDefault
from django.conf import settings
from django.http import HttpResponse
from .forms import FileFieldForm
from django.utils.timezone import now as timezone_now
# from django.core.validators import FileExtensionValidator
# Create your models here.
# def rand_off(length=30):
# 		if length <= 0:
# 			length = 30
# 		symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits
# 		return ''.join([random.choice(symbols) for x in range(length)])

# def upload_to(instance, filename):
# 	now = timezone_now()
# 	filename_base, filename_ext = os.path.splitext(filename)
# 	return 'files/{}_{}{}'.format(now.strftime("%Y/%m/%d/%Y%m%d%H%M%S"),rand_off(),filename_ext.lower())		
# def Form(request):
# 		return render(request,"index/form.html",{})

# def Upload(request):
# 	for count,x in enumerate(request.FILES.getlist("files")):
# 		def process(f):
# 			with open(settings.FILES_ROOT + 'file_' + str(count), 'wb+') as destination:
# 				for chunk in f.chunks():
# 					destination.write(chunk)
# 		process(x)
# 	return HttpResponse("Files(s) uploded!")
class News(AbstractDefault):
	def update_image(instance, filename):
		image_path = settings.IMAGES_ROOT
		# format = instance.userid + instance.transaction_uuid + instance.file_extension
		# return os.path.join(path, format)
		image_root=image_path+"news_"+filename
		# return 'user_{0}/{1}'.format(instance.user.id, filename)
		return image_root

	def update_video(instance, filename):
		video_path = settings.VIDEOS_ROOT	   
		video_root=video_path+"news_"+filename
		return video_root

	def update_file(instance, filename):
		file_path = settings.DOCUMENT_ROOT
		file_root=file_path+"news_"+filename
		# print filename.getlist
		return file_root

	news_title = models.CharField(verbose_name = 'Title', max_length = 255)
	news_description = models.TextField(verbose_name = 'Description', max_length = 1000)
	# news_image = models.ImageField(verbose_name = 'Images', upload_to = update_image,validators=[FileExtensionValidator(['png','jpeg','jpg'])])
	# news_video = models.FileField(verbose_name = 'Video',blank=True, upload_to = update_video,validators=[FileExtensionValidator(['mp4'])]) 
	# news_document = models.FileField(verbose_name = 'Document',blank=True, null = True, upload_to = update_file,validators=[FileExtensionValidator(['docx','pdf'])])
	news_image = models.ImageField(verbose_name = 'Images',upload_to = update_image)
	news_video = models.FileField(verbose_name = 'Video',blank=True,upload_to = update_video) 
	# news_document = models.FileField(verbose_name = 'Document',blank=True, null = True, upload_to = update_file)
	news_document = models.FileField(verbose_name = 'Document',blank=True,upload_to = update_file)

	def __str__(self):
		return self.news_title

	def clean_image(self):
		news_image = self.cleaned_data.get('news_image',False)
		print 'imgsize_'+ news_image._size
		return

	@property
	def filename(self):
		name = self.file.name.split("/")[1].replace('_',' ').replace('-',' ')
		return name
	def get_absolute_url(self):
		return reverse('myapp:document-detail', kwargs={'pk': self.pk})

	class Meta:
		verbose_name = "New"
		verbose_name_plural = "News"
		ordering = ['id']

