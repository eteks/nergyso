# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from employee.models import Employee
from master.models import AbstractDefault
from django.db.models.signals import post_save, pre_save
from master.models import Notification
from push_notifications.models import APNSDevice, GCMDevice

# Create your models here.
class Shoutout(AbstractDefault):
	shoutout_description = models.TextField(verbose_name = 'Description', max_length = 1000)
	shoutout_employee_from = models.ForeignKey(Employee,verbose_name = 'Employee From',related_name='Employee_From')
	shoutout_employee_to = models.ForeignKey(Employee,verbose_name = 'Employee To',related_name='Employee_To')
	shoutout_approval_status = models.BooleanField(verbose_name = 'Shoutout Approve By Admin', default = False)

	def __str__(self):
		return self.shoutout_description #updated by kalai

	class Meta:
		verbose_name = "Shoutout"
        verbose_name_plural = "Shoutouts"
        ordering = ['id']

def pre_save_shoutout(sender, instance, **kwargs):
	print "pre_save_shoutout"
	global shoutout_approval_status
	shoutout_approval_status = 0
	print instance.shoutout_approval_status
	if instance.pk is not None:
		print "instance pk not none"
		shoutout_approval_status = instance.shoutout_approval_status

def save_shoutout(sender, instance, **kwargs):
	print "save_shoutout"
	emp_id = Employee.objects.all().values_list('user_ptr_id', flat=True)
	# print(emp_id)
	cateogry = "Shoutout"
	cateogry_id=Notification.objects.filter(notification_cateogry=cateogry,notification_cateogry_id=instance.id).exists()
	# print event_id
	# if cateogry_id:   
	# 	pass
	# else:
	print "shoutout_approval_status"
	print shoutout_approval_status
	if shoutout_approval_status == 1:
		for p in emp_id:
			note = Notification(notification_cateogry=cateogry,notification_cateogry_id=instance.id,notification_delivery_status=0,notification_read_status=0,notification_created_date=instance.created_date,notification_employee_id=p)
			# print note
			note.save()
			print shoutout_approval_status
			try:
				devices = GCMDevice.objects.get(user=p)
				devices.send_message(instance.shoutout_employee_from.username+" is posted Shoutout for "+instance.shoutout_employee_to.username,title="New Shoutout posted",extra={"shoutout_id": instance.id,"category":"shoutout","notification_id":note.id})
			except GCMDevice.DoesNotExist:
				pass	
		# devices = GCMDevice.objects.all()
		# for q in devices:
		# 	q.send_message(instance.shoutout_employee_from.username+" is posted Shoutout for "+instance.shoutout_employee_to.username,title="New Shoutout posted",extra={"shoutout_id": instance.id,"category":"shoutout"})
		# print(p)

post_save.connect(save_shoutout, sender=Shoutout)

pre_save.connect(pre_save_shoutout, sender=Shoutout)