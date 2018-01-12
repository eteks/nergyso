def handle_uploaded_file(f,product):
  filename, file_ext = splitext(basename(f.name))
  suf = SimpleUploadedFile(filename + file_ext,f.read())
  product.photos.save(filename + '_photo' + file_ext, suf, save=False)
  
from django.core.files.uploadedfile import SimpleUploadedFile
def create_path_for_photos_thumbanails(photos, product):
 #Creating path for large photos
 photosgroup = ''
 count=len(photos)
 for uploaded_file in photos:
  count=count-1
  handle_uploaded_file(uploaded_file,product)
  if count==0:
   photosgroup=photosgroup + str(product.photos)
  else:
   photosgroup=photosgroup + str(product.photos) + ','
 large_photos=photosgroup
 print "large_photos", large_photos
 
 # Creating path for thumbnail photos
 photo=str(large_photos)
 photos=photo.split(',')
 
 imagecount= len(photos)
 print "imagecount", imagecount
 
 thumbnail_group=''
 if large_photos:
  try:
   count =len(photos)
   for photo in photos:
    print "photos", photo
    count=count-1
    THUMBNAIL_SIZE = (400, 400) # dimensions
    image = ImageObj.open(settings.MEDIA_ROOT + '/' + photo)
    print "image", image
    print "THUMBNAIL_SIZE", THUMBNAIL_SIZE
    # Convert to RGB if necessary
    if image.mode not in ('L', 'RGB'): image = image.convert('RGB')
    # create a thumbnail + use antialiasing for a smoother thumbnail
    image.thumbnail(THUMBNAIL_SIZE, ImageObj.ANTIALIAS)
    # fetch image into memory
    temp_handle = StringIO()
    # print "temp", temp_handle
    image.save(temp_handle, 'png')
    temp_handle.seek(0)
    disassembled = urlparse(photo)
    filename, file_ext = splitext(basename(disassembled.path))
    suf = SimpleUploadedFile(filename + file_ext, temp_handle.read(), content_type='image/png')
    product.thumbnail.save(filename + '_thumbnail' +'.png', suf, save=False)
    # print product.thumbnail
    if count == 0:
     thumbnail_group = thumbnail_group + str(product.thumbnail)
    else:
     thumbnail_group = thumbnail_group + str(product.thumbnail) + ','
   # print thumbnail_group
  except ImportError:
   pass
 thumbnail_photos = thumbnail_group 
 return large_photos, imagecount, thumbnail_photos          
 return large_photos, imagecount

 product.photos, product.imagecount, product.thumbnail = create_path_for_photos_thumbanails(photos, product)

 from __future__ import unicode_literals

from django.contrib import admin

from models import Gallery
from forms import GalleryFileForm
from energysoft.action import export_as_csv_action
from django.conf import settings
# from django.core.files.uploadedfile import SimpleUploadedFile
# import os
# # Register your models here.
# def handle_uploaded_file(f):
#   filename, file_ext = os.path.splitext(f.name)
#   suf = SimpleUploadedFile(filename + file_ext,f.read())
#   Gallery().gallery_image.save(filename + '_photo' + file_ext, suf, save=False) 

class GalleryAdmin(admin.ModelAdmin):
  model = Gallery
  form= GalleryFileForm
  list_display = ('gallery_title','created_date','gal_image',)
  search_fields = ('gallery_title',)
  actions = [export_as_csv_action("CSV Export", fields=['id','gallery_title','created_date'])]

  def save_model(self,request,obj,form,change):   
    for count, x in enumerate(request.FILES.getlist("gallery_image")):
      print x
      def process(f):
        with open('media/images/' + str(count), 'wb+') as destination:
          for chunk in f.chunks():          
            destination.write(chunk)
      # handle_uploaded_file(x)
      # if count==0:
      #   filer=str(x)
      # else:
      #   filer=str(x) + ','
      # print filer
      
    # files = request.FILES.getlist('gallery_image')
    # for x in files:     
      
      # process(x)

admin.site.register(Gallery, GalleryAdmin)

# for count, x in enumerate(request.FILES.getlist("gallery_image")):
    #   def process(f):
    #     with open('media/images/file_' + str(x), 'wb+') as destination:
    #       for chunk in f.chunks():          
    #         destination.write(chunk)
    #   process(x)
    #   if count==0:
    #     filer=str(x)
    #   else:
    #     filer=str(x) + ','
    #   print filer
    # obj.gallery_title;