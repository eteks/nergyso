# from django import forms
# from django.contrib.auth.models import User
# from models import Employee
# class EmployeeForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(EmployeeForm, self).__init__(*args, **kwargs)
#         self.fields['username'] = forms.ChoiceField(
#             choices=[(o.id, str(o)) for o in User.objects.all()]
#         )
#     class Meta:
#         model = Employee
#         fields = '__all__'