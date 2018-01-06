from django.contrib import admin
from models import Banner
from forms import BannerFileForm
# Register your models here.
class BannerAdmin(admin.ModelAdmin):
	model = Banner
	form= BannerFileForm
	list_display = ('created_date','ban_image')

admin.site.register(Banner,BannerAdmin)
