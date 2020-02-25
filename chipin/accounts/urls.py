from django.urls import path
from accounts.views import SignUpView, UpdateProfileView, DetailProfileView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('detail_profile/<str:pk>/<str:slug>', DetailProfileView.as_view(), name='profile_detail'),
    path('update_profile/<str:pk>/<str:slug>', UpdateProfileView.as_view(), name='update_profile'),
]
