from __future__ import unicode_literals

from django.db import models
from forms import BannerFileForm
from master.models import AbstractDefault
from django.conf import settings
# from employee.models import Employee

# Create your models here.
def update_image(instance, filename):
	image_path = settings.IMAGES_ROOT
	image_root=image_path+"banner_"+filename
	# emp_id = Employee.objects.all().values_list('employee_id', flat=True)
	# for p in emp_id:
	# 	print(p)
	# files = filename
	# print "hi"+files
	return image_root

class Banner(AbstractDefault):
	banner_image = models.FileField(verbose_name = 'Banner Image',upload_to = update_image,help_text="Supports Only jpg/png/jpeg format.(size 790px * 350px)")

	
	def ban_image(self):
		count=len(str(self.banner_image))
		filer=''
		if count > 0:
			return '<img src="'+settings.SITE_URL+'%s" width="100px"/>' % self.banner_image
		else:
			return 'none'
	ban_image.allow_tags = True
	ban_image.short_description = 'Image'

	
def __str__(self):
	return self.id
