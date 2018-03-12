# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from master.models import AbstractDefault
from embed_video.fields import EmbedVideoField
from employee.models import Employee
from master.models import Notification
from django.db.models.signals import post_save
from push_notifications.models import APNSDevice, GCMDevice
# Create your models here.
class Livetelecast(AbstractDefault):
	livetelecast_title = models.CharField(verbose_name = 'Title', max_length = 255,help_text="Ex:Promotion Live")
	livetelecast_url = EmbedVideoField(verbose_name = 'Embed Livecast URL',help_text="Ex:https://youtu.be/SKo2B8Vf53M")
	
	def __str__(self):
		return self.livetelecast_url

	class Meta:
		verbose_name = "Livetelecast"
        verbose_name_plural = "Livetelecasts"
        ordering = ['id']

def save_livetelecast(sender, instance, **kwargs):
	emp_id = Employee.objects.all().values_list('user_ptr_id', flat=True)
	# print(emp_id)
	cateogry = "Livetelecast"
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
			q.send_message(instance.livetelecast_title, title="New Live Telecast posted",extra={"live_id": instance.id,"category":"livetelecast"})
		# print(p)

post_save.connect(save_livetelecast, sender=Livetelecast)