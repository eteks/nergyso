# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from master.models import AbstractDefault
from embed_video.fields import EmbedVideoField

# Create your models here.
class Livetelecast(AbstractDefault):
	livetelecast_url = EmbedVideoField(verbose_name = 'Embed Livecast URL')
	
	def __str__(self):
		return self.livetelecast_url

	class Meta:
		verbose_name = "Livetelecast"
        verbose_name_plural = "Livetelecasts"
        ordering = ['id']

