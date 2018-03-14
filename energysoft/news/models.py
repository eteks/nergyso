from __future__ import unicode_literals

from django.db import models
from master.models import AbstractDefault
from django.conf import settings
from forms import FileFieldForm
from django.core.exceptions import ValidationError
from employee.models import Employee
from master.models import Notification
from django.db.models.signals import post_save
from push_notifications.models import APNSDevice, GCMDevice
# print current_site_url()

def update_image(instance, filename):
	image_path = settings.IMAGES_ROOT
	image_root=image_path+"news_"+filename
	return image_root

def update_video(instance, filename):
	video_path = settings.VIDEOS_ROOT	   
	video_root=video_path+"news_"+filename
	return video_root

def update_file(instance, filename):
	file_path = settings.DOCUMENT_ROOT
	file_root=file_path+"news_"+filename
	return file_root

class NewsManager(models.Manager):
    def get_queryset(self):
        # return super(NewsManager, self).get_queryset().annotate(total_points=Sum('points__value'))
		return super(NewsManager, self).get_queryset().order_by('-id')

class News(AbstractDefault):
	news_title = models.CharField(verbose_name = 'Title', max_length = 255,help_text="Ex:Report")
	news_description = models.TextField(verbose_name = 'Description', max_length = 1000,help_text="Ex:News description")
	news_image = models.ImageField(verbose_name = 'Images',upload_to = update_image,help_text="Ex:Supports Only jpg/png/jpeg format.")
	news_video = models.FileField(verbose_name = 'Video',upload_to = update_video) 
	news_document = models.FileField(verbose_name = 'Document',upload_to = update_file)

	objects = NewsManager()

	def __str__(self):
		return self.news_title

	def gal_image(self):
		files = str(self.news_image).split(',')
		count=len(files)
		filer=''
		if count > 1:
			for x in files:
				filer = filer + '<img src="'+settings.SITE_URL+'%s" width="100px"/>' % str(x) + '&nbsp;'
			return filer
		else:
			return 'None'
	gal_image.allow_tags = True
	gal_image.short_description = 'Image'

	class Meta:
		verbose_name = "New"
		verbose_name_plural = "News"
		ordering = ['id']

def save_news(sender, instance, **kwargs):
	emp_id = Employee.objects.all().values_list('user_ptr_id', flat=True)
	# print(emp_id)
	cateogry = "News"
	cateogry_id=Notification.objects.filter(notification_cateogry=cateogry,notification_cateogry_id=instance.id).exists()
	# print event_id
	if cateogry_id:   
		pass
	else:
		for p in emp_id:
			note = Notification(notification_cateogry=cateogry,notification_cateogry_id=instance.id,notification_delivery_status=0,notification_read_status=0,notification_created_date=instance.created_date,notification_employee_id=p)
			# print note
			note.save()
			devices = GCMDevice.objects.get(user=p)
			devices.send_message(instance.news_title, title="News posted",extra={"news_id": instance.id,"category":"news","notification_id":note.id})

# def save_news(sender, instance, **kwargs):
# 	emp_id = Employee.objects.all().values_list('user_ptr_id', flat=True)
# 	# print(emp_id)
# 	cateogry = "News"
# 	cateogry_id=Notification.objects.filter(notification_cateogry=cateogry,notification_cateogry_id=instance.id).exists()
# 	# print event_id
# 	if cateogry_id:   
# 		pass
# 	else:
# 		for p in emp_id:
# 			note = Notification(notification_cateogry=cateogry,notification_cateogry_id=instance.id,notification_delivery_status=0,notification_read_status=0,notification_created_date=instance.created_date,notification_employee_id=p)
# 			# print note
# 			note.save()
# 		devices = GCMDevice.objects.all()
# 		for q in devices:
# 			q.send_message(instance.news_title, title="News posted",extra={"news_id": instance.id,"category":"news"})
		# print(p)

post_save.connect(save_news, sender=News)