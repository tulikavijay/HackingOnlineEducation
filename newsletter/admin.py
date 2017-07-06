# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# add from .forms import model_form_name
# add class model_name_Admin(admin.ModelAdmin)
# this changes the look of the admin page containing db
# add list_display=["__unicode__","field2","field3"..]
# form=model_form_name
# admin.site.register(model_name,model_name_Admin)
from .forms import SignUpForm
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    list_display=["__unicode__","full_name","email"]
    form=SignUpForm

admin.site.register(SignUp,SignUpAdmin)
