# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from embed_video.fields import EmbedVideoField
from forms import EventFileForm
from django.conf import settings
from master.models import AbstractDefault,Department
from employee.models import Employee
from master.models import Notification
from django.db.models.signals import post_save
from push_notifications.models import APNSDevice, GCMDevice
# Create your models here.
def update_image(instance, filename):
	image_path = settings.IMAGES_ROOT
	image_root=image_path+"events_"+filename
	return image_root

def update_video(instance, filename):
	video_path = settings.VIDEOS_ROOT	   
	video_root=video_path+"events_"+filename
	return video_root

def update_file(instance, filename):
	file_path = settings.DOCUMENT_ROOT
	file_root=file_path+"events_"+filename
	return file_root

class EventsManager(models.Manager):
    def get_queryset(self):
        # return super(NewsManager, self).get_queryset().annotate(total_points=Sum('points__value'))
		return super(EventsManager, self).get_queryset().order_by('-id')

class Events(AbstractDefault):
	events_title = models.CharField(verbose_name = 'Title', max_length = 255,help_text="Ex:Celebration")
	events_description = models.TextField(verbose_name = 'Description', max_length = 1000,help_text="Details about Event")
	events_location_for_map = models.CharField(verbose_name = 'Location', max_length = 255,help_text="Ex:Chennai")
	events_venue = models.CharField(verbose_name = 'Venue', max_length = 255,help_text="Ex:Hilton")
	events_date = models.DateTimeField(verbose_name = 'Events Date')
	events_image = models.ImageField(verbose_name = 'Images',upload_to = update_image,help_text="Supports Only jpg/png/jpeg format.")
	events_video = models.FileField(verbose_name = 'Video',upload_to = update_video) 
	events_document = models.FileField(verbose_name = 'Document',upload_to = update_file)

	objects = EventsManager()

	def __str__(self):
		return self.events_title

	class Meta:
		verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['id']

def save_events(sender, instance, **kwargs):
	emp_id = Employee.objects.all().values_list('user_ptr_id', flat=True)
	# print(emp_id)
	cateogry = "Events"
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
			q.send_message(instance.events_title, title="New Events posted",extra={"events_id": instance.id,"category":"events"})
		# print(p)

post_save.connect(save_events, sender=Events)