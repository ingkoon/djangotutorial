from django.db import models
from django.db.models.fields import BooleanField, CharField, DateField, DateTimeField, IntegerField

# Create your models here.
class contents(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    write_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    views = models.IntegerField(default= 0)
    weather = models.CharField(max_length=10)
    api_emotion = models.CharField(max_length=10)
    result_emotion = models.CharField(max_length=30)
    user_pick = models.BooleanField()
