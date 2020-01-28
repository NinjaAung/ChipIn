from django.urls import path
from landing.views import LandingView

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
]

