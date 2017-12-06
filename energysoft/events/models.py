# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from embed_video.fields import EmbedVideoField
from master.models import AbstractDefault,Department

# Create your models here.

class Events(AbstractDefault):
	events_title = models.CharField(verbose_name = 'Title', max_length = 255)
	events_description = models.TextField(verbose_name = 'Description', max_length = 1000)
	events_location = models.CharField(verbose_name = 'Location', max_length = 255)
	events_venue = models.CharField(verbose_name = 'Venue', max_length = 255)
	events_image = models.ImageField(verbose_name = 'Images', upload_to = 'images/events')
	events_video = EmbedVideoField(verbose_name = 'Video') 
	events_document = models.FileField(verbose_name = 'Document', upload_to = 'files/events')
	events_date = models.DateTimeField(verbose_name = 'Date')

	def __str__(self):
		return self.events_title

	class Meta:
		verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['id']