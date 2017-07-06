# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#sign up form for newsletter not login or contact
class SignUp(models.Model):
     full_name=models.CharField(max_length=60,blank=True)
     email=models.EmailField()

     def __unicode__(self):
         return self.email
