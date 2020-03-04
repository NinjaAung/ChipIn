from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import Profile, MonthlyDonation
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
'email', 'password1', 'password2',)

class SetupProfileForm(ModelForm):
    monthly_donation = forms.DecimalField(max_digits=8, decimal_places=2, help_text='Monthly Donation')
     
    class Meta:
         model = Profile
         fields = ('monthly_donation',)

class CreateMonthlyDonationForm(ModelForm):
    monthly_donation = forms.DecimalField(max_digits=8, decimal_places=2, help_text='Monthly Donation')
    
    class Meta:
         model = MonthlyDonation
         fields = ('monthly_donation',)






