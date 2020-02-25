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
from accounts.models import Profile


class PortfolioView(LoginRequiredMixin, ListView):
    """ Renders a list of all Pages. """
    model = Cause
   
    def get(self, request):
        """ GET a list of Pages. """
        causes = self.get_queryset().all()
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