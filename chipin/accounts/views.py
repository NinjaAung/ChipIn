from django.shortcuts import render
from django.contrib.auth import login, authenticate
from accounts.forms import SignUpForm, SetupProfileForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from accounts.models import Profile
from django.views.generic.detail import DetailView

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UpdateProfileView(UpdateView):
    model = Profile 
    form_class = SetupProfileForm
    template_name = 'update_profile.html'
    success_url = reverse_lazy('portfolio')


class DetailProfileView(DetailView):
    model = Profile
    template_name = 'detail_profile.html'

    def get_queryset(self):
        return Profile.objects.filter()

    def get(self, request, pk, slug):
        
        
        return render(request, self.template_name, {'nonprofs' : orgs_list_dict, 'value': value})
