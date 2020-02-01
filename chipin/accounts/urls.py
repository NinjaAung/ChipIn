from django.urls import path
from accounts.views import profile_view, signup_view


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('profile/', profile_view, name='profile'),
]