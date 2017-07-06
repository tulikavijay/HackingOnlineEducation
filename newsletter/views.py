# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.
def signup(request):
    form=SignUpForm
    instance=form.save(commit=False)
    email=form.clean_email()
    name=form.clean_fullname()
    if form is_valid :
        instance.save()
        context{
        'title':'Sign up for our newsletter'
        'form' : form
        }
    return render(request,'signup.html',context)
