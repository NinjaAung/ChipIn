from django.urls import path
from accounts.views import SignUpView, UpdateProfileView, DetailProfileView, CreateMonthlyDonationView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('detail_profile/<str:pk>/<str:slug>', DetailProfileView.as_view(), name='detail_profile'),
    path('update_profile/<str:pk>/<str:slug>', UpdateProfileView.as_view(), name='update_profile'),
    path('create_monthly_donation/', CreateMonthlyDonationView.as_view(), name='create_monthly_donation'),
]
