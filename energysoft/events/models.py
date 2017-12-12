# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from embed_video.fields import EmbedVideoField
from master.models import AbstractDefault,Department

# Create your models here.

class EventsManager(models.Manager):
    def get_queryset(self):
        # return super(NewsManager, self).get_queryset().annotate(total_points=Sum('points__value'))
		return super(EventsManager, self).get_queryset().order_by('-id')

class Events(AbstractDefault):
	events_title = models.CharField(verbose_name = 'Title', max_length = 255)
	events_description = models.TextField(verbose_name = 'Description', max_length = 1000)
	events_location_for_map = models.CharField(verbose_name = 'Location', max_length = 255)
	events_venue = models.CharField(verbose_name = 'Venue', max_length = 255)
	events_date = models.DateTimeField(verbose_name = 'Events Date')
	events_image = models.ImageField(verbose_name = 'Images', upload_to = 'images/events')
	events_video = models.FileField(verbose_name = 'Video',upload_to = 'video/events/') 
	events_document = models.FileField(verbose_name = 'Document', upload_to = 'files/events')

	objects = EventsManager()

	def __str__(self):
		return self.events_title

	class Meta:
		verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['id']