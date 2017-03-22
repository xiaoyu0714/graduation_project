# In forms.py...
from django import forms
from user_app.models import Object

class UploadFileForm(forms.Form):
    obj_name = forms.CharField(label='名称',max_length=50)
    obj_num = forms.IntegerField(label='数量')
