from django import forms
    
class CommentForm(forms.Form):
    nick=forms.CharField(id='nick',label=u'Ник',max_length='20',required='True')
    capcha=forms.CharField(id='capcha',label=u'Капча',,required='True')
    message=forms.CharField(id='message',label=u'Комментарий', widget=forms.Textarea(attrs={'rows':9, 'cols':60,'wrap':'soft'}),required='True')
