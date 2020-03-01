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
import math
import random

class PortfolioView(LoginRequiredMixin, ListView):
    """ Renders a list of all Pages. """
    model = Cause

    def get(self, request):
        """ GET a list of Pages. """
        profile_values = Value.objects.filter(user=request.user).values('value')
        monthly_donation = MonthlyDonation.objects.filter(user=request.user).values('amount')
        if profile_values.count() < 3: 
          return HttpResponseRedirect(reverse('create_value'))
        elif monthly_donation.count() == 0: 
          return HttpResponseRedirect(reverse('create_monthly_donation'))
        else: 
          amount = monthly_donation.first().get('amount') 
          category_list = []
          for value in profile_values:
            value = value.get('value')
            category_list.append(value)
          donation_amount = float(amount) * 0.10
          category = random.choice(category_list)
          causes = []
          for i in range(10):
            category = random.choice(category_list)
            cause = self.get_queryset().filter(category=category)[:1]
            causes.append(cause)
          return render(request, 'portfolio.html', {
            'causes': causes
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