from django.db import models

class Amalker(models.Model):
    text = models.TextField(null=True, blank=True)
    kateg = models.CharField(max_length=250) # указывается предмет или список ...ов коллекции
    time = models.DateTimeField(auto_now_add=True, db_index=True)
    info = models.CharField(max_length=250)
    
