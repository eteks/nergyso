# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Employee(User):
	employee_employeeId = models.PositiveIntegerField(verbose_name = 'Employee ID')
	employee_employeeName = models.CharField(verbose_name = 'Employee Name', max_length = 255)
	employee_dateOfBirth = models.DateTimeField(verbose_name = 'Date of Birth')
	employee_email = models.EmailField(verbose_name = 'Email ID', max_length = 255)
	employee_mobileNumber = models.CharField(verbose_name = 'Mobile Number', max_length = 10)
	employee_dateOfJoining = models.DateTimeField(verbose_name = 'Date of Joining')
	employee_designation = models.CharField(verbose_name = 'Designation', max_length = 255)
	employee_photo = models.ImageField(verbose_name = 'Profile pic', upload_to = 'images/profile/')
	employee_bloodGroup = models.CharField(verbose_name = 'Blood Group',max_length = 255)
	employee_address = models.TextField(verbose_name = 'Address',max_length = 1000)
	employee_aadharId = models.PositiveIntegerField(verbose_name = 'Aadhar ID')
	employee_departmentId = models.CharField(verbose_name = 'Employee Department ID',max_length = 255)
	employee_experience = models.PositiveIntegerField(verbose_name = 'No. of Years experienced')

	def __str__(self):
		return self.employee_employeeId

	class Meta:
		verbose_name = "Employee"
        verbose_name_plural = "Employee"
        ordering = ['id']

