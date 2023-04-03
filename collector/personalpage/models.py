from django.db import models


class NewArticle(models.Model):
    title = models.CharField( max_length=100, null=True, blank=True)
    text = models.TextField( blank=False, null=False) 
    photo = models.FileField(null=True, blank=True)

