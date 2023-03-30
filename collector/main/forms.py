from django import forms
from django.forms.forms import Form 

class ProstoList(Form):
    pole = forms.CharField(min_length=2, max_length=150) 
