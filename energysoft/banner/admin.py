from __future__ import unicode_literals

from django.contrib import admin
from models import Banner
from forms import BannerFileForm
# Register your models here.

class BannerAdmin(admin.ModelAdmin):
	model = Banner
	list_display = ('created_date','ban_image',)
	fields = ( 'ban_image', )
	readonly_fields = ('ban_image',)
	list_filter = ('created_date',)

admin.site.register(Banner,BannerAdmin)
