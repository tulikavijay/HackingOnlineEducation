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
    phone=models.CharField(max_length=10)
    designation=models.CharField(max_length=20)
    image=models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username

class Categories(models.Model):
    category_name=models.CharField(max_length=30,null=False)
    url=models.URLField()
    description=models.TextField()
    rating=models.IntegerField()
    image=models.ImageField(upload_to='categories', blank=True)
    def __unicode__(self):
        return self.category_name

class Pages(models.Model):
    category=models.ForeignKey(Categories,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=30,null=False)
    rating=models.IntegerField()
    url=models.URLField()
    def __unicode__(self):
        return self.name
