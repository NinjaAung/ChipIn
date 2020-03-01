from django.shortcuts import render
from django.contrib.auth import login, authenticate
from accounts.forms import SignUpForm, SetupProfileForm, CreateMonthlyDonationForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from accounts.models import Profile, MonthlyDonation
from django.views.generic.detail import DetailView
from django.forms import formset_factory
from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class CreateMonthlyDonationView(CreateView):
    model = MonthlyDonation
    template_name = 'update_profile.html'
    form_class = CreateMonthlyDonationForm
    success_url = reverse_lazy('portfolio')

    def form_valid(self, form_class):
        monthlydonation = form_class.save(commit=False)
        monthlydonaton.user = self.request.user
        return super(CreateMonthlyDonationView, self).form_valid(form_class)
        
class UpdateProfileView(UpdateView):
    model = Profile 
    form_class = SetupProfileForm
    template_name = 'update_profile.html'
    success_url = reverse_lazy('portfolio')

class DetailProfileView(DetailView):
    model = Profile
    template_name = 'detail_profile.html'


    def get(self, request, slug):
      """ Returns a specific wiki page by slug. """
      value = Value.objects.filter(user=request.user)
      return render(request, template_name, {
          'value': value
        })

    def get(self, request, pk, slug):
        return render(request, self.template_name)
