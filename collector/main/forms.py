from django import forms
from django.forms.forms import Form 

class ProstoList(Form):
    pole = forms.CharField(min_length=2, max_length=150) 

class CommentUser(Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':20}), label='Комментировать') 
    
class CommentForComment(Form):
    comment2 = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':20})) 
    comment2_id = forms.CharField(min_length=1, max_length=150) # ид статьи
    # comment2_id_id = forms.CharField(min_length=1, max_length=150) # ид коммента