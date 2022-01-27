from cProfile import Profile
from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.forms.formsets import formset_factory
from .models import *

# class RegisterForm(UserCreationForm):
#     xyz = forms.BooleanField()

#     class Meta:
#         model =User
#         fields = ('username', 'xyz')

class choiceForm(forms.Form):
    CHOICES = [('true', 'True'),
               ('false', 'False'),
               ('none', 'None')]

    eee = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    class Meta:
        fields = ('eee',)

    # def save(self, commit=True):
    #     user = super(choiceForm, self).save(commit=False)
    #     user.eee = self.cleaned_data["eee"]
    #     if commit:
    #         user.save()
    #     return user

    # def save(self, commit=True):
    #     m = super(choiceForm, self).save(commit=False)
    #     for i in self.eee:
    #         m = Profile(self)
    #         m.identify = i
    #     if commit:
    #         m.save()
    #     return m
    

class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ("username", "password1")

   

  