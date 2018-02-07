from __future__ import unicode_literals
from django import forms
import os
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from models import Employee


def validate_image(employee_photo):    
    file_size = employee_photo._size
    ext = os.path.splitext(employee_photo.name)[1]
    valid_extensions = settings.IMAGE_TYPES
    if not ext.lower() in valid_extensions:
        raise ValidationError('Supports Only jpg/png/jpeg format.')
    if file_size > settings.MAX_UPLOAD_SIZE:
        raise ValidationError("Image file size should be less than 2 mb")

class EmpFileForm(forms.ModelForm):
    # events_document = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    # password = forms.CharField(widget=forms.PasswordInput)
    
    employee_photo = forms.ImageField(validators=[validate_image])

    # def __init__(self, *args, **kwargs):
    #     super(EmpFileForm, self).__init__(*args, **kwargs)
    #     self.fields['username'] = forms.ChoiceField(
    #     choices=[(o.id, str(o)) for o in User.objects.all()]
    #     )
    # class Meta:
    #     model = Employee
    #     fields = '__all__'


