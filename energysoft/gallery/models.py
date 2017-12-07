# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from master.config import GALLERY_CATEGORY
from master.models import AbstractDefault

# Create your models here.
class Gallery(AbstractDefault):
	gallery_title = models.CharField(verbose_name = 'Title', max_length = 255)
	gallery_image = models.ImageField(verbose_name = 'Image', upload_to = 'images/gallery/')
	gallery_category = models.CharField(verbose_name = 'Gallery Category', choices=GALLERY_CATEGORY,max_length=50)

	def __str__(self):
		return self.gallery_title

	class Meta:
		verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
        ordering = ['id']
