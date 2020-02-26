from django.shortcuts import render
from django.contrib.auth import login, authenticate
from accounts.forms import SignUpForm, SetupProfileForm, CreateValueForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from accounts.models import Profile, Value
from django.views.generic.detail import DetailView

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class CreateValueView(CreateView):
    model = Value
    template_name = 'create_value.html'
    form_class = CreateValueForm
    success_url = reverse_lazy('portfolio')


    def form_valid(self, form_class):
        value = form_class.save(commit=False)
        value.user = self.request.user
        #article.save()  # This is redundant, see comments.
        return super(CreateValueView, self).form_valid(form_class)


class UpdateProfileView(UpdateView):
    model = Profile 
    form_class = SetupProfileForm
    template_name = 'update_profile.html'
    success_url = reverse_lazy('portfolio')

    # def get_object(self, )


class DetailProfileView(DetailView):
    model = Profile
    template_name = 'detail_profile.html'

    def cause_detail_view(request, primary_key):
        model = Value

    def get(self, request, slug):
      """ Returns a specific wiki page by slug. """
      value = Value.objects.filter(user=request.user)
      return render(request, template_name, {
          'value': value
        })

    def get(self, request, pk, slug):
        return render(request, self.template_name)
