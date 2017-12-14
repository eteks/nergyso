# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from master.models import AbstractDefault
from employee.models import Employee
from master.config import FEEDBACK_CATEGORY

# Create your models here.
class Feedback(AbstractDefault):
	feedback_description = models.TextField(verbose_name = 'Description', max_length = 1000)
	#updated by kalai
	feedback_queries = models.TextField(verbose_name = 'Queries', max_length = 500)
	feedback_employee = models.ForeignKey(Employee,verbose_name = 'Employee')
	feedback_category = models.CharField(verbose_name = 'Feedback Category', choices=FEEDBACK_CATEGORY,max_length=50)
	#updated by kalai
	feedback_category_id = models.IntegerField(verbose_name = 'Category Id',null=True,help_text="It stores the events or news id",blank=True) #Feedback catgory id contains events id
	feedback_rating_count = models.IntegerField(verbose_name = 'Feedback Rating') #Feedback catgory id contains events id
	feedback_approval_status = models.BooleanField(verbose_name = 'Feedback Approve By Admin', default = False)

	def __str__(self):
		return self.feedback_description

	class Meta:
		verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"
        ordering = ['id']
