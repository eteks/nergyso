# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from employee.models import Employee
from master.models import AbstractDefault

# Create your models here.
class Shoutout(AbstractDefault):
	shoutout_description = models.TextField(verbose_name = 'Description', max_length = 1000)
	shoutout_employee = models.ForeignKey(Employee,verbose_name = 'Employee')
	shoutout_approval_status = models.BooleanField(verbose_name = 'Shoutout Approve By Admin', default = False)

	def __str__(self):
		return self.shoutout_description #updated by kalai

	class Meta:
		verbose_name = "Shoutout"
        verbose_name_plural = "Shoutouts"
        ordering = ['id']