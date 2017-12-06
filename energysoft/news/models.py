# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from embed_video.fields import EmbedVideoField
from master.models import AbstractDefault

# Create your models here.
		
class News(AbstractDefault):
	news_title = models.CharField(verbose_name = 'Title', max_length = 255)
	news_description = models.TextField(verbose_name = 'Description', max_length = 1000)
	news_image = models.ImageField(verbose_name = 'Images', upload_to = 'images/news/')
	news_video = models.FileField(verbose_name = 'Video',upload_to = 'images/news/') 
	news_document = models.FileField(verbose_name = 'Document', null = True, upload_to = 'files/news/')

	def __str__(self):
		return self.news_title

	class Meta:
		verbose_name = "New"
        verbose_name_plural = "News"
        ordering = ['id']

