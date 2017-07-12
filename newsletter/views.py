# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render
from .forms import SignUpForm,UserForm,UserProfileForm
from django.contrib.auth.decorators import login_required
#importing models
from .models import UserProfile
# Create your views here.
def home(request):
    return render(request,'home.html',{'title':'Welcome','dashboard':'DashBoard'})

def signup(request):
    form=SignUpForm(request.POST or None)
    context={
    'title':'Sign up for our newsletter',
    'form' : form,
    }
    instance=form.save(commit=False)
    if form.is_valid() :
        instance.save()
        context={
        'title':'Thank you!'
        }
    return render(request,'signup.html',context)

def register(request):

    registered=False
    if request.method =='POST':
        user_form=UserForm(request.POST or None)
        profile_form=UserProfileForm(request.POST or None,request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user_form.cleaned_data.get('password'))
            username=user_form.cleaned_data.get('username')
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model

            if 'image' in request.FILES:
                profile.image = request.FILES['image']
                # Now we save the UserProfile model instance.
                profile.save()

            # Update our variable to tell the template registration was successful.
                registered=True
                login(request,user)
                #return render(request,'userprofile.html',{'profile_picture':profile.picture,
                #'username':username})
            else:
                print user_form.errors or profile_form.errors
    else:
        user_form=UserForm()
        profile_form=UserProfileForm()

    return render(request,'register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})


def contact(request):
    return render(request,'contact.html',{})
#def contact(request):
    #title="Send a Message"
    #form=ContactForm(request.POST or None)
    #if form.is_valid():
     #  email=form.cleaned_data.get('Email')
      # message=form.cleaned_data.get('message')
       #to_email=[email]
      # print(email,message)
      # send_mail('Reply message',message,settings.EMAIL_HOST_USER,to_email,fail_silently=False)
    #context={
     #"form":form,
     #"title":title,
    #}
    #return render(request,'contact.html',context)

def explore(request):
    context={}
    return render(request,'categories.html',context)


@login_required
def profile(request):
    #user=get_object_or_404(User,user_username=self.kwargs['username'])
    model=UserProfile
    userprofile=UserProfile.objects.get(user=request.user)
    context={
    'user':request.user,
    'userprofile':userprofile
    }
    return render(request,'dashboard.html',context)
