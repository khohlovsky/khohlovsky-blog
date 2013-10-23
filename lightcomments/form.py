#encoding:utf-8
from django import forms
    
class CommentForm(forms.Form):
    nick=forms.CharField(max_length=20,label="nick",widget=forms.TextInput(attrs={'placeholder':'nickname'}))
    capcha=forms.CharField('capcha',label='capcha',required='True')
    message=forms.CharField('message',label='comment',
    widget=forms.Textarea(attrs={'rows':9,
    'cols':60,'wrap':'soft','placeholder':'add your message'}),required='True')
