from django import forms
from django.forms.forms import Form 

class ProstoList(Form):
    pole = forms.CharField(min_length=2, max_length=150) 

class CommemtUser(Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':20}), label='Комментировать') 