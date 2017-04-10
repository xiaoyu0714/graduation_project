from django import forms
from user_app.models import Object,User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from .notify_const import object_notify,person_notify
import re

class UploadFileForm(forms.Form):
    obj_name = forms.CharField(label='名称',max_length=50)
    obj_num = forms.IntegerField(label='数量')
    desc = forms.CharField(label='描述',max_length=100)
    file = forms.FileField()

    def clean(self):
        cleaned_data = super(UploadFileForm,self).clean()
        num = cleaned_data['obj_num']
        if num <= 0:
            self.add_error('obj_num',object_notify['ILLEGAL_OBJECT_NUMBER'])

class UserForm(forms.ModelForm):
    phone_regex = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
    class Meta:
        model = User
        fields = ['nickname','phone','head_pic','school','personal_intro']

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        phone = cleaned_data['phone']
        phone_valid = UserForm.phone_regex.match(phone)
        if not phone_valid:
            self.add_error('phone',person_notify['ILLEGAL_PHONE'])
