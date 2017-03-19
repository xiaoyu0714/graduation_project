# In forms.py...
from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(label='title',max_length=50)
    file = forms.FileField()
