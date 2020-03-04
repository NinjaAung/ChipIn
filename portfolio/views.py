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
from itertools import chain


class PortfolioView(LoginRequiredMixin, ListView):
    """ Renders a list of all Pages. """
    model = Cause

    def generate_portfolio(self, request):
      profile_values = Value.objects.filter(user=request.user).values('value')
      category_list = []
      for value in profile_values:
        value = value.get('value')
        category_list.append(value)
      print(profile_values)
      
      print(category_list)
      causes = self.get_queryset().filter(category__in=category_list)
      return causes
      


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
          causes = self.generate_portfolio(request)
          print(causes)
          return render(request, 'portfolio.html', {
            'causes': causes
          })




          

          



          
          # # cause1 = self.get_queryset().filter(category=random.choice(category_list))
          # cause1 = self.get_queryset().filter(category='Government Accountability')

               

      
    
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