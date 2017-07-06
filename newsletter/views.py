# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.
def home(request):
    return render(request,'home.html',{'title':'Welcome'})

def signup(request):
    form=SignUpForm(request.POST or None)
    instance=form.save(commit=False)
    context={}
    if form.is_valid() :
        instance.save()
        context={
        'title':'Sign up for our newsletter',
        'form' : form
        }
    return render(request,'signup.html',context)
