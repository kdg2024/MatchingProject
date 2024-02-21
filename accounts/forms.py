from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = CustomUser
    fields = ('username', 'password1', 'password2', 'registration_type')

class CustomUserEditForm(forms.ModelForm):
  class Meta:
    model = CustomUser
    fields = ("last_name", "first_name", "registration_type","profile")
