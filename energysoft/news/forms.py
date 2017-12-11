from django import forms

class FileFieldForm(forms.ModelForm):
    news_document = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    # def clean_image(self):
    #      news_image = self.cleaned_data.get('news_image',False)
    #      print 'imgsize_'+ news_image._size
    #      if news_image:
    #          if news_image._size > 4*1024*1024:
    #                raise ValidationError("Image file too large ( > 4mb )")
    #          return news_image
    #      else:
    #          raise ValidationError("Couldn't read uploaded image")