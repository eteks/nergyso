# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from master.models import AbstractDefault, Department
from django.core.validators import MinValueValidator

def update_image(instance, filename):
	image_path = settings.IMAGES_ROOT
	image_root=image_path+"emp_"+filename
	return image_root
	
class EmployeeManager(models.Manager):
    def get_queryset(self):
        # return super(NewsManager, self).get_queryset().annotate(total_points=Sum('points__value'))
		return super(EmployeeManager, self).get_queryset().order_by('-user_ptr_id')

# Create your models here.
class Employee(User,AbstractDefault):
	# username = models.OneToOneField(User, on_delete=models.CASCADE)
	employee_id = models.CharField(verbose_name = 'Employee ID',max_length=15,unique=True,help_text="Ex:Emp_id_001")
	employee_name = models.CharField(verbose_name = 'Employee Name', max_length = 255,help_text="Ex:Claris")
	employee_dob = models.DateField(verbose_name = 'Date of Birth')
	# employee_email = models.EmailField(verbose_name = 'Email ID', max_length = 255)
	employee_mobile = models.CharField(verbose_name = 'Mobile Number', max_length = 10,help_text="Ex:9944919023")
	employee_doj = models.DateField(verbose_name = 'Date of Joining')
	employee_department = models.ForeignKey(Department,verbose_name = 'Department',help_text="Ex:Management")
	employee_designation = models.CharField(verbose_name = 'Designation', max_length = 255,help_text="Ex:HR")
	employee_photo = models.ImageField(verbose_name = 'Profile Image', upload_to = update_image,help_text="Supports Only jpg/png/jpeg format.")
	employee_bloodgroup = models.CharField(verbose_name = 'Blood Group',max_length = 255,help_text="Ex:A+")
	employee_address = models.TextField(verbose_name = 'Address',max_length = 1000)
	# employee_aadhar_id = models.IntegerField(verbose_name = 'Aadhar ID',)	
	employee_experience_in_years = models.IntegerField(verbose_name = 'No. of Years experienced',help_text="Ex:4")
	employee_device_id = models.CharField(verbose_name = 'Device Id',max_length = 255)

	objects = EmployeeManager()

	def __str__(self):
		return self.user_ptr_id

	def gal_image(self):
		return '<img src="'+settings.SITE_URL+'%s" width="100px"/>' % self.employee_photo
	gal_image.allow_tags = True
	gal_image.short_description = 'Image'
	# def save(self):
	# 	user=User.objects.get(username=self.username)
	# 	user.email=self.employee_email
	# 	user.save()
	
	# def set_password(self, password):
	# 	self.password = make_password(raw_password)
	# 	self.save()
	# 	return self
	# def make_password(password):
	# 	from random import random
	# 	algo = 'sha1'
	# 	salt = get_hexdigest(algo, str(random()), str(random()))[:5]
	# 	hash = get_hexdigest(algo, salt, password)
	# 	return '%s$%s$%s' % (algo, salt, hash)
	
	class Meta:
		verbose_name = "Employee"
        verbose_name_plural = "Employee"
        ordering = ['id']

