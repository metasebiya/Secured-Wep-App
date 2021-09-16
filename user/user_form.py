from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserRegisterForm(UserCreationForm):
    firstName = forms.CharField(max_length=10, required=True, help_text='Optional')
    lastName = forms.CharField(max_length=10, required=True, help_text='Optional')
    username = forms.CharField(max_length=10, required=True, help_text='Optional')
    email = forms.EmailField(max_length=120, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'username', 'email', 'password1', 'password2')
