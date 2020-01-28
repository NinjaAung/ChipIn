from django.shortcuts import render
from django.views.generic import CreateView


class LandingView(CreateView):
    """ Class to render landingpage. """

    def get(self, request):
        """ returns landing page. """
        return render(request, 'index.html')
