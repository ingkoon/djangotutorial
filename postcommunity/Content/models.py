from django.db import models

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=100, null = True)
    author = models.CharField( max_length=30, null = True)
    whather = models.CharField(max_length= 10, null = True)
    body = models.TextField(blank=True, null=True)
    result_emotion = models.models.CharField(max_length=50)
    
    
    
    