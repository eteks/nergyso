# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from embed_video.admin import AdminVideoMixin
# from django.shortcuts import redirect, render
# from django.shortcuts import render_to_response
from .models import News
from forms import FileFieldForm

# Register your models here.

# def add_attachment(request):
# 	if request.method == "POST":
# 		parent_id = request.POST['parent_id']
# 		files = request.FILES.getlist('myfiles')
# 		for a_file in files:
# 			instance = Attachment(
# 				parent_id=parent_id,
# 				file_name=a_file.name,
# 				attachment=a_file
# 			)
# 			instance.save()
# 		return redirect("add_attachment_done")
# 	return render(request, "add_attachment.html")

# def add_attachment_done(request):
# 	return render_to_response('add_attachment_done.html')

class NewsAdmin(AdminVideoMixin, admin.ModelAdmin):
	# pass
	form= FileFieldForm

admin.site.register(News, NewsAdmin)
