# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate,logout,update_session_auth_hash
from django.shortcuts import render
from .forms import SignUpForm,UserForm,UserProfileForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponse
#from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
#importing models
from .models import UserProfile,Categories,Pages,Course,StandAlone,Challenge
from star_ratings.models import Rating,UserRating
# Create your views here.
def home(request):
    import top_stories
    stories=top_stories.stories[:6]
    context={}
    challenges=Categories.objects.filter(sort='challenges',ratings__isnull=False).order_by('-ratings__average')[:4]
    standalones=Categories.objects.filter(sort='standalones')
    category_list = Categories.objects.filter(sort='courses',ratings__isnull=False).order_by('-ratings__average')[:4]
    pages=Pages.objects.order_by('-ratings__average')[:5]
    added = {
     'categories': category_list,
     'challenges':challenges,
     'standalones':standalones,
     'title':'Welcome',
     'pages':pages,
     'stories':stories
    }
    context.update(added)
    return render(request,'home.html',context)

def challenges(request):
    challenges=Categories.objects.filter(sort='challenges').order_by('-ratings__average')
    context={
    'challenges':challenges
    }
    return render(request,'challenges.html',context)

def signup(request):
    context={}
    form=SignUpForm(request.POST or None)
    instance=form.save(commit=False)
    if form.is_valid() :
        instance.save()
        context={
        'title':'Thank you!',
        'form':''
        }
    else :
        context={
        'title':'Sign up for our newsletter',
        'form' : form,
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
    model=Categories
    categories=Categories.objects.filter(sort='courses').order_by('-ratings__average')
    context={
    'categories':categories
    }
    return render(request,'categories.html',context)

def category(request,category_name):
    #category=Categories.objects.get(category_name=category)
    model=Pages
    category=Categories.objects.get(category_name=category_name)
    pages=Pages.objects.filter(category=category)
    context={
    'category':category,
    'pages':pages,
    }
    return render(request,'category.html',context)

def search(request):
    query=request.GET.get("q")
    searchc={}
    searchp=Pages.objects.filter(name__iexact=query).order_by('-ratings__average')
    context={
    'searchp':searchp
    }
    if not searchp :
        try :
            searchc=Categories.objects.get(category_name__iexact=query)
            context.update({'searchc':searchc})
        except :
            pass
        else :
            pass

    if not searchc and not searchp :
        context.update({'search':'Query Not Found'})

    return render(request,'search.html',context)

def articles(request):
    import top_stories
    stories=top_stories.stories
    context={'stories':stories}
    return render(request,'articles.html',context)

@login_required

def rating_courses(request,category_name):
    model=Pages
    category=Categories.objects.get(category_name=category_name)
    pages=Pages.objects.filter(category=category)
    context={
    'category':category,
    'pages':pages,
    }
    return render(request,'rate.html',context)

@login_required
def profile(request):
    #user=get_object_or_404(User,user_username=self.kwargs['username'])
    model=UserProfile
    courses=UserRating.objects.filter(user=request.user)
    userprofile=UserProfile.objects.get(user=request.user)
    context={
    'user':request.user,
    'userprofile':userprofile,
    'courses':courses
    }
    return render(request,'dashboard.html',context)

@login_required
def enroll(request):
    model=Pages
    categories=Categories.objects.filter(sort='courses' or 'challenges');
    pages=Pages.objects.all();
    context={'pages':pages,'categories':categories}
    return render(request,'enroll.html',context)

@login_required
def add(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        id=request.POST.get('id','')
        category=request.POST.get('category','')
        print('name=',name)
        user=User.objects.get(username=request.user)
        if name and category:
            page_added=Course.create(
            user=user,
            course=name,
            timestamp=datetime.now()
            )
    return HttpResponse('')
# def rating(request):
#     if request.method=='POST':
#         new_rating=0
#         print(request.POST.get('page',''))
#         course=request.POST.get('page','')
#         category_name=request.POST.get('category_name','')
#         rating=request.POST.get('rate','0')
#         print(course,category_name,rating)
#         user=User.objects.get(username=request.user)
#         if rating and course :
#             course=Course.create(
#             user=user,
#             course=course,
#             timestamp=datetime.now()
#             )
#             category=Categories.objects.get(category_name=category_name)
#             page=Pages.objects.get(category=category,name=course)
#             new_rating=((page.rating)+int(rating))/2
#             page.rating=new_rating
#             page.save()
#
#     return HttpResponse('')
