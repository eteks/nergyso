from __future__ import unicode_literals
from django import forms
import os
from django.conf import settings
from django.core.exceptions import ValidationError

def validate_image(events_image):    
    file_size = events_image._size
    ext = os.path.splitext(events_image.name)[1]
    valid_extensions = settings.IMAGE_TYPES
    if not ext.lower() in valid_extensions:
        raise ValidationError('Supports Only jpg/png/jpeg format.')
    if file_size > settings.MAX_UPLOAD_SIZE:
        raise ValidationError("Image file size should be less than 2 mb")

def validate_video(events_video):
    file_size = events_video._size
    ext = os.path.splitext(events_video.name)[1]
    valid_extensions = settings.VIDEO_TYPES
    if not ext.lower() in valid_extensions:
        raise ValidationError('Supports Only mp4 format.')
    if file_size > settings.MAX_VIDEO_SIZE:
        raise ValidationError("Image file size should be less than 50 mb")

def validate_document(events_document):
    file_size = events_document._size
    ext = os.path.splitext(events_document.name)[1]
    valid_extensions = settings.DOCUMENT_TYPES
    if not ext.lower() in valid_extensions:
        raise ValidationError('Supports Only doc/docx/pdf format.')
    if file_size > settings.MAX_UPLOAD_SIZE:
        raise ValidationError("Image file size should be less than 2 mb")

class EventFileForm(forms.ModelForm):
    # events_document = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    events_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}),validators=[validate_image])
    events_video = forms.FileField(validators=[validate_video],required=False)    
    events_document = forms.FileField(validators=[validate_document],required=False)
