# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Events
from forms import EventFileForm
from energysoft.action import export_as_csv_action
from django.conf import settings
import os
from django.core.files.uploadedfile import SimpleUploadedFile

# Register your models here.
def handle_uploaded_file(f):
    filename, file_ext = os.path.splitext(f.name)
    suf = SimpleUploadedFile(filename + file_ext,f.read())
    Events().events_image.save(filename + file_ext, suf, save=False)
# Register your models here.
# class EventsAdmin(AdminVideoMixin, admin.ModelAdmin):
# 	pass

class EventsAdmin(admin.ModelAdmin):
    # default value of all parameters:
    model = Events
    form= EventFileForm
    list_display = ('events_title','events_venue','events_date')
    list_filter = ('events_title','events_date',)
    search_fields = ('events_title','events_venue',)
    actions = [export_as_csv_action("CSV Export", fields=['events_title','events_venue','events_date','events_description'])]

    def save_model(self,request,obj,form,change,*args,**kwargs):
        count=len(request.FILES.getlist("events_image"))       
        # print count
        filer=''
        files = request.FILES.getlist('events_image')
        for x in files:
            count=count-1
            if count==0:
                filer = filer + settings.IMAGES_ROOT + 'events_'+ str(x)
            else:
                filer = filer + settings.IMAGES_ROOT + 'events_'+ str(x) + ','
            handle_uploaded_file(x)

        obj.events_image = filer
        super(Events, obj).save(*args,**kwargs)
    

admin.site.register(Events, EventsAdmin)
