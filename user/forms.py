from django import forms
from .models import Users

class LoginForm(forms.Form):
    account = forms.CharField(max_length=32, label='账号')
    password = forms.CharField(max_length=20, label='密码')

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'account', 'password', 'phone',
                  'role_id']
        labels = {'username': '用户名',
                  'account': '账号',
                  'password': '密码',
                  'phone': '电话',
                  'role_id': '角色',
                  }
