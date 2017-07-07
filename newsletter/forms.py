from django import forms
from .models import SignUp,User,UserProfile

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
    class Meta():
        model=User
        fields=['full_name','email','password']

class UserProfileForm():
    class Meta():
        model=UserProfile
        fields=['user_name','image']
