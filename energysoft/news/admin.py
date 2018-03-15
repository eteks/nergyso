# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from energysoft.action import export_as_csv_action
# from django.shortcuts import redirect, render
# from django.shortcuts import render_to_response
from .models import News
from forms import FileFieldForm
from django.conf import settings
import os
from django.core.files.uploadedfile import SimpleUploadedFile
from master.models import Notification
from django.contrib.admin.actions import delete_selected
#Required import for delete selected actions
from django.contrib import messages
from django.contrib.admin import helpers
from django.contrib.admin.utils import get_deleted_objects, model_ngettext
from django.core.exceptions import PermissionDenied
from django.db import router
from django.template.response import TemplateResponse
from django.utils.encoding import force_text
from django.utils.translation import ugettext as _, ugettext_lazy

def handle_uploaded_file(f):
    filename, file_ext = os.path.splitext(f.name)
    suf = SimpleUploadedFile(filename + file_ext,f.read())
    News().news_image.save(filename + file_ext, suf, save=False)

class NewsAdmin(AdminVideoMixin, admin.ModelAdmin):
	# pass
	model = News
	form= FileFieldForm
	fields = ('active_status','delete_status','news_title','news_description','news_image','gal_image',)
	readonly_fields = ['gal_image']
	list_display = ('news_title','created_date','modified_date')
	list_filter = ('news_title',)
	search_fields = ('news_title',)
	actions = [export_as_csv_action("CSV Export", fields=['id','news_title','news_description','created_date']),'delete_selected']

	def save_model(self,request,obj,form,change,*args,**kwargs):
		counts=len(request.FILES.getlist("news_image"))
		count=counts 
        # print count
		filer=''
		files = request.FILES.getlist('news_image')
		for x in files:
			count=count-1
			if count==0:
				filer = filer + settings.IMAGES_ROOT + 'news_'+ str(x)
			else:
				filer = filer + settings.IMAGES_ROOT + 'news_'+ str(x) + ','
			handle_uploaded_file(x)
		if counts!=0:	
			obj.news_image = filer
		super(News, obj).save(*args,**kwargs)


	def delete_model(self,request,obj,*args,**kwargs):
		Notification.objects.filter(notification_cateogry_id=obj.id,notification_cateogry__icontains="news").delete()
		obj.delete()

	def delete_selected(modeladmin, request, queryset):
	    """
	    Default action which deletes the selected objects.

	    This action first displays a confirmation page which shows all the
	    deletable objects, or, if the user has no permission one of the related
	    childs (foreignkeys), a "permission denied" message.

	    Next, it deletes all selected objects and redirects back to the change list.
	    """
	    opts = modeladmin.model._meta
	    app_label = opts.app_label

	    # Check that the user has delete permission for the actual model
	    if not modeladmin.has_delete_permission(request):
	        raise PermissionDenied

	    using = router.db_for_write(modeladmin.model)

	    # Populate deletable_objects, a data structure of all related objects that
	    # will also be deleted.
	    deletable_objects, model_count, perms_needed, protected = get_deleted_objects(
	        queryset, opts, request.user, modeladmin.admin_site, using)

	    # The user has already confirmed the deletion.
	    # Do the deletion and return a None to display the change list view again.
	    if request.POST.get('post') and not protected:
	        if perms_needed:
	            raise PermissionDenied
	        n = queryset.count()
	        if n:
	            for obj in queryset:
	            	#Custom code to deleted mapped id in notification table
	            	Notification.objects.filter(notification_cateogry_id=obj.id,notification_cateogry__icontains="news").delete()
	                obj_display = force_text(obj)
	                modeladmin.log_deletion(request, obj, obj_display)
	            queryset.delete()
	            modeladmin.message_user(request, _("Successfully deleted %(count)d %(items)s.") % {
	                "count": n, "items": model_ngettext(modeladmin.opts, n)
	            }, messages.SUCCESS)
	        # Return None to display the change list page again.
	        return None

	    if len(queryset) == 1:
	        objects_name = force_text(opts.verbose_name)
	    else:
	        objects_name = force_text(opts.verbose_name_plural)

	    if perms_needed or protected:
	        title = _("Cannot delete %(name)s") % {"name": objects_name}
	    else:
	        title = _("Are you sure?")

	    context = dict(
	        modeladmin.admin_site.each_context(request),
	        title=title,
	        objects_name=objects_name,
	        deletable_objects=[deletable_objects],
	        model_count=dict(model_count).items(),
	        queryset=queryset,
	        perms_lacking=perms_needed,
	        protected=protected,
	        opts=opts,
	        action_checkbox_name=helpers.ACTION_CHECKBOX_NAME,
	        media=modeladmin.media,
	    )

	    request.current_app = modeladmin.admin_site.name

	    # Display the confirmation page
	    return TemplateResponse(request, modeladmin.delete_selected_confirmation_template or [
	        "admin/%s/%s/delete_selected_confirmation.html" % (app_label, opts.model_name),
	        "admin/%s/delete_selected_confirmation.html" % app_label,
	        "admin/delete_selected_confirmation.html"
	    ], context)


delete_selected.short_description = ugettext_lazy("Delete selected %(verbose_name_plural)s")
	
admin.site.register(News, NewsAdmin)
