from django.db import models

# Create your models here.


class user(models.Model):
    use_id = models.IntegerField(unique = True)
    user_name = models.CharField()
    user_location = models.CharField()
    user_real_location = models.CharField()
    user_point = models.IntegerField()
    matching = models.BooleanField()

    def __str__(self):
        return self.name