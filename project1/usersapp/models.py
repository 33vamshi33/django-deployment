from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userprofileinfo(models.Model):

    #create releationship with user dont inherit
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    #adding additional attributes
    portfolio=models.URLField(blank=True)
    picture=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):

        #from admin user to we are getting username
        return self.user.username

