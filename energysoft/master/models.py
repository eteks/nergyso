# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from master.config import NOTIFICATION_CATEGORY
from push_notifications.models import APNSDevice, GCMDevice
from django.db.models.signals import post_save

#Master model to use in throughout website
class AbstractDefault(models.Model):
	active_status = models.BooleanField(verbose_name = 'Active Status', default = False)
	delete_status = models.BooleanField(verbose_name = 'Delete status', default = False)
	created_date = models.DateTimeField(auto_now_add=True, help_text="Auto generated by system.")
	modified_date = models.DateTimeField(auto_now_add=True, help_text="Auto generated by system.")

	class Meta:
		abstract = True

class Department(AbstractDefault):
	department_name = models.CharField(verbose_name = 'Department Name',max_length=50)

	def __str__(self):
		return self.department_name

class Notification(models.Model):
	from employee.models import Employee
	notification_cateogry = models.CharField(max_length=50,verbose_name = 'Notification Category',choices=NOTIFICATION_CATEGORY)
	notification_cateogry_id = models.IntegerField(verbose_name = 'Notification Category Id',null=True) #It may be map the id from events or news or shoutout
	notification_employee = models.ForeignKey(Employee,verbose_name='Employee')
	# notification_message = models.CharField(max_length=200,verbose_name='Notification message',help_text='It will be used only for CEO',blank=True)
	notification_delivery_status = models.BooleanField(verbose_name = 'Notification Delivery Status', default = False)
	notification_read_status = models.BooleanField(verbose_name = 'Notification Read Status', default = False)
	notification_created_date = models.DateTimeField(auto_now_add=True, help_text="Auto generated by system.")

	def __str__(self):
		return self.notification_cateogry

class CEOMessage(models.Model):
	from employee.models import Employee
	ceo_message = models.CharField(max_length=200,verbose_name='CEO message',unique=True)
	ceo_employee = models.ForeignKey(Employee,verbose_name='CEO Name')
	active_status = models.BooleanField(verbose_name = 'Active Status', default = True)
	delete_status = models.BooleanField(verbose_name = 'Delete status', default = False)
	created_date = models.DateTimeField(auto_now_add=True, help_text="Auto generated by system.")
	modified_date = models.DateTimeField(auto_now_add=True, help_text="Auto generated by system.")
		
	def __str__(self):
		return self.ceo_message

def save_ceomessage(sender, instance, **kwargs):
	from employee.models import Employee
	emp_id = Employee.objects.all().values_list('user_ptr_id', flat=True)
	# print(emp_id)
	cateogry = "ceo"
	cateogry_id=Notification.objects.filter(notification_cateogry=cateogry,notification_cateogry_id=instance.id).exists()
	# print event_id
	if cateogry_id:   
		pass
	else:
		for p in emp_id:
			note = Notification(notification_cateogry=cateogry,notification_cateogry_id=instance.id,notification_delivery_status=0,notification_read_status=0,notification_created_date=instance.created_date,notification_employee_id=p)
			# print note
			note.save()
		devices = GCMDevice.objects.all()
		for q in devices:
			q.send_message(instance.ceo_message, title="New message got from CEO",extra={"ceomessage_id": instance.id,"category":"ceo"})
		# print(p)

post_save.connect(save_ceomessage, sender=CEOMessage)