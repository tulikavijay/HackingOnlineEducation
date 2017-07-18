from django import forms
from .models import SignUp,User,UserProfile,Categories,Pages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class SignUpForm(forms.ModelForm):
    class Meta():
        model=SignUp
        fields=['full_name','email']

    def clean_email(self):
        email=self.cleaned_data.get('email')
        return email

    def clean_fullname(self):
        full_name=self.cleaned_data.get('full_name')
        return full_name

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['username','email','password']

class UserProfileForm(forms.ModelForm):
    class Meta():
        model=UserProfile
        fields=['designation','phone','image']

class CategoriesForm(forms.ModelForm):
    class Meta():
        model=Categories
        fields=['category_name','url','rating','description','sort','image']

class PagesForm(forms.ModelForm):
    class Meta():
        model=Pages
        fields=['name','url','rating','category']

# class EditProfileForm(forms.ModelForm):
#     user=forms.CharField(required=True)
#     email=forms.EmailField(required=True)
#     # phone=forms.CharField(required=False)
#     # designation=forms.CharField(required=False)
#
#     class Meta():
#         model=User
#         fields=['username','email']
#     def save(self,commit=True):
#             user=super(UserProfileForm,self).save(commit=False)
#             user.email=self.cleaned_data.get('email')
#             user.username=self.cleaned_data.get('username')
#             if commit:
#                 user.save()
#             return user




#class ContactForm(forms.Form):
    #    name=forms.CharField(max_length=20,required=False)
    #    Email=forms.EmailField()
    #    message=forms.CharField(max_length=120)
