# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Events
from multiupload.admin import MultiUploadAdmin
from forms import EventFileForm
from energysoft.action import export_as_csv_action

# Register your models here.
# class EventsAdmin(AdminVideoMixin, admin.ModelAdmin):
# 	pass

class EventsAdmin(MultiUploadAdmin):
    # default value of all parameters:
    model = Events
    form= EventFileForm
    list_display = ('events_title','events_venue','events_date')
    list_filter = ('events_title','events_date',)
    search_fields = ('events_title','events_venue',)
    actions = [export_as_csv_action("CSV Export", fields=['events_title','events_venue','events_date','events_description'])]
    change_form_template = 'multiupload/change_form.html'
    change_list_template = 'multiupload/change_list.html'
    multiupload_template = 'multiupload/upload.html'
    # if true, enable multiupload on list screen
    # generaly used when the model is the uploaded element
    multiupload_list = True
    # if true enable multiupload on edit screen
    # generaly used when the model is a container for uploaded files
    # eg: gallery
    # can upload files direct inside a gallery.
    multiupload_form = True
    # max allowed filesize for uploads in bytes
    multiupload_maxfilesize = 3 * 2 ** 20 # 3 Mb
    # min allowed filesize for uploads in bytes
    multiupload_minfilesize = 0
    # tuple with mimetype accepted
    multiupload_acceptedformats = ( "image/jpeg",
                                    "image/pjpeg",
                                    "image/png",)

    def process_uploaded_file(self, uploaded, object, request,**kwargs):
        '''
        Process uploaded file
        Parameters:
            uploaded: File that was uploaded
            object: parent object where multiupload is
            request: request Object
        Must return a dict with:
        return {
            'url': 'url to download the file',
            'thumbnail_url': 'some url for an image_thumbnail or icon',
            'id': 'id of instance created in this method',
            'name': 'the name of created file',

            # optionals
            "size": "filesize",
            "type": "file content type",
            "delete_type": "POST",
            "error" = 'Error message or jQueryFileUpload Error code'
        }
        '''
        print "process_uploaded_file"
        print uploaded
        # example:
        title = kwargs.get('title', [''])[0] or uploaded.name
        f = self.model(events_image=uploaded, events_title=title)
        f.save()
        # return {
        #     'url': f.image_thumb(),
        #     'thumbnail_url': f.image_thumb(),
        #     'id': f.id,
        #     'name': f.title
        # }
        return {
            # 'url': f.image_thumb(),
            # 'thumbnail_url': f.image_thumb(),
            'id': f.id,
            'name': f.events_title
        }

    def delete_file(self, pk, request):
        '''
        Function to delete a file.
        '''
        # This is the default implementation.
        obj = get_object_or_404(self.queryset(request), pk=pk)
        obj.delete()

admin.site.register(Events, EventsAdmin)
