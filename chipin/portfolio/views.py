from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from portfolio.models import Cause
from accounts.models import Profile
import requests
import random 
import json
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Profile, MonthlyDonation
from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse
from value.models import Value

class PortfolioView(LoginRequiredMixin, ListView):
    """ Renders a list of all Pages. """
    model = Cause

    def get(self, request):
        """ GET a list of Pages. """
        causes = self.get_queryset().all() 
        # monthly_donation = Profile.objects.filter(user=request.user.profile.monthly_donation)
        monthly_donation = MonthlyDonation.objects.filter(user=request.user)
        profile_values = Value.objects.filter(user=request.user)
        if profile_values.count() < 3: 
          return HttpResponseRedirect(reverse('create_value'))
        elif monthly_donation.count() == 0: 
          return HttpResponseRedirect(reverse('create_monthly_donation'))
        else: 
          return render(request, 'portfolio.html', {
          'causes': causes,
          'profile_values': profile_values
        })
    
class CauseDetailView(LoginRequiredMixin, DetailView):
  model = Cause
  template_name = 'cause_detail.html'

  def cause_detail_view(request, primary_key):
    model = Page

    def get(self, request, slug):
      """ Returns a specific wiki page by slug. """
      cause = self.get_queryset().get(slug__iexact=slug)
      return render(request, template_name, {
          'cause': cause
        })