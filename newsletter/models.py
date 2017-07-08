# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#sign up form for newsletter not login or contact
class SignUp(models.Model):
     full_name=models.CharField(max_length=60,blank=True)
     email=models.EmailField()

     def __unicode__(self):
         return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #user_name=models.CharField(max_length=60)
    image=models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.user_name
