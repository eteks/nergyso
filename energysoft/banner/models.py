from __future__ import unicode_literals

from django.db import models
from master.models import AbstractDefault

# Create your models here.

class Banner(AbstractDefault):
	banner_image = models.FileField(verbose_name = 'Banner Image')

	def __str__(self):
		return self.banner_id
