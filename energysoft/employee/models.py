# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from master.models import AbstractDefault, Department

# Create your models here.
class Employee(User,AbstractDefault):
	employee_id = models.CharField(verbose_name = 'Employee ID',max_length=15)
	employee_name = models.CharField(verbose_name = 'Employee Name', max_length = 255)
	employee_dob = models.DateField(verbose_name = 'Date of Birth')
	employee_email = models.EmailField(verbose_name = 'Email ID', max_length = 255)
	employee_mobile = models.CharField(verbose_name = 'Mobile Number', max_length = 10)
	employee_doj = models.DateField(verbose_name = 'Date of Joining')
	employee_department = models.ForeignKey(Department,verbose_name = 'Department')
	employee_designation = models.CharField(verbose_name = 'Designation', max_length = 255)
	employee_photo = models.ImageField(verbose_name = 'Profile Image', upload_to = 'images/profile/')
	employee_bloodgroup = models.CharField(verbose_name = 'Blood Group',max_length = 255)
	employee_address = models.TextField(verbose_name = 'Address',max_length = 1000)
	employee_aadhar_id = models.PositiveIntegerField(verbose_name = 'Aadhar ID')	
	employee_experience_in_years = models.PositiveIntegerField(verbose_name = 'No. of Years experienced')
	employee_device_id = models.CharField(verbose_name = 'Device Id',max_length = 255)

	def __str__(self):
		return self.user_ptr_id

	class Meta:
		verbose_name = "Employee"
        verbose_name_plural = "Employee"
        ordering = ['id']

