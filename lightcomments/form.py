#encoding:utf-8
from django import forms
    
class CommentForm(forms.Form):
    nick=forms.CharField(maxlentght=20)
    capcha=forms.CharField('capcha',label=u'Капча',required='True')
    message=forms.CharField('message',label=u'Комментарий', widget=forms.Textarea(attrs={'rows':9, 'cols':60,'wrap':'soft'}),required='True')
