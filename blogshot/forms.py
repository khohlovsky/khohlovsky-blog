# coding:utf-8
from django import forms

class LoginForm(forms.Form):
   login=forms.CharField(label=u'Логин:',)
   password=forms.CharField(widget=forms.PasswordInput(),label=u'Пароль')
