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
from .forms import SignUpForm,UserForm,UserProfileForm,CategoriesForm,PagesForm
from .models import SignUp,User,UserProfile,Categories,Pages,Course,StandAlone,Challenge,Code100

class SignUpAdmin(admin.ModelAdmin):
    list_display=["__unicode__","full_name","email"]
    form=SignUpForm

#class UserAdmin(admin.ModelAdmin):
#    list_display=["__unicode__","full_name","email"]
#    form=UserForm

class UserProfileAdmin(admin.ModelAdmin):
    list_display=["__unicode__","designation","phone","image"]
    form=UserProfileForm

class CategoriesAdmin(admin.ModelAdmin):
    list_display=["__unicode__","url","rating","description","image","sort"]
    form=CategoriesForm

class PagesAdmin(admin.ModelAdmin):
    list_display=["__unicode__","url","rating"]
    form=PagesForm

class CourseAdmin(admin.ModelAdmin):
    list_display=["__unicode__","timestamp","date"]

class StandAloneAdmin(admin.ModelAdmin):
    list_display=["__unicode__","url","description","image"]

class ChallengeAdmin(admin.ModelAdmin):
    list_display=["__unicode__","url","rating","description","image"]

class Code100Admin(admin.ModelAdmin):
    list_display=["user","started","timestamp","done"]


admin.site.register(SignUp,SignUpAdmin)
admin.site.register(Categories,CategoriesAdmin)
admin.site.register(Pages,PagesAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Challenge,ChallengeAdmin)
admin.site.register(StandAlone,StandAloneAdmin)
admin.site.register(Code100,Code100Admin)
#admin.site.register(User,UserAdmin)

admin.site.register(UserProfile,UserProfileAdmin)
