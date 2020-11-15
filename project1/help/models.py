from django.db import models

# Create your models here.
class user(models.Model):
    first_name=models.CharField(max_length=264)
    last_name=models.CharField(max_length=264)
    e_mail=models.EmailField(unique=True)

    def __str__(self):
        return self.first_name