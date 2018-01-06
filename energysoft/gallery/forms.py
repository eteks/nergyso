from __future__ import unicode_literals
from django import forms
import os
from django.conf import settings
from django.core.exceptions import ValidationError

def validate_image(gallery_image):    
    file_size = gallery_image._size
    ext = os.path.splitext(gallery_image.name)[1]
    valid_extensions = settings.IMAGE_TYPES
    if not ext.lower() in valid_extensions:
        raise ValidationError('Supports Only jpg/png/jpeg format.')
    if file_size > settings.MAX_UPLOAD_SIZE:
        raise ValidationError("Image file size should be less than 2 mb")

class GalleryFileForm(forms.ModelForm):
    # events_document = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    gallery_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}),validators=[validate_image])

    def post(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		files = request.FILES.getlist('gallery_image')
		if form.is_valid():
		    for f in files:
		        print f
		    return self.form_valid(form)
		else:
			return self.form_invalid(form)