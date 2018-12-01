# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Staff

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Staff
        fields = ('username', 'email', 'role', 'groups')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Staff
        fields = ('username', 'email')