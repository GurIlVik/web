from django import forms
from django.forms.forms import Form 

class ProstoList(Form):
    pole = forms.CharField(min_length=2, max_length=150) 


    




# from django.contrib.auth.models import User
# from django import forms
# from django.core.exceptions import ValidationError 
# from django.forms.forms import Form 

# class Collectible_for_user(Form):
#     collectible_objects = forms.CharField(min_length=3)  # заготовка пока без результата
    
# class ProstoList(Form):
#     pole = forms.CharField(min_length=2, max_length=150) 
   