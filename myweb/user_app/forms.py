from django import forms
from user_app.models import Object,User

class UploadFileForm(forms.Form):
    obj_name = forms.CharField(label='名称',max_length=50)
    obj_num = forms.IntegerField(label='数量')
    desc = forms.CharField(label='描述',max_length=100)
    file = forms.FileField()

class UserForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ['nickname','phone','head_pic','school','personal_intro']
