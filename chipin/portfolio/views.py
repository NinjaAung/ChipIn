from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from portfolio.models import Cause
from django.views.generic.list import ListView
import requests
import random 
import json
from django.http import HttpResponseRedirect




class PortfolioView(ListView):
    """ Renders a list of all Pages. """
    model = Cause

    def get(self, request):
        """ GET a list of Pages. """
        causes = self.get_queryset().all()
        return render(request, 'portfolio.html', {
          'causes': causes
        })
