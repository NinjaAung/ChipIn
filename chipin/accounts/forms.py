from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import Value, Payment 
from django.db.models.signals import post_save
from django.dispatch import receiver

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
'email', 'password1', 'password2',)


class CreateValueForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = Value
        fields = ('value',)


