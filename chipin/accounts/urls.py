from django.urls import path
from accounts.views import SignUpView, UpdateProfileView, DetailProfileView, CreateValueView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('detail_profile/<str:pk>/<str:slug>', DetailProfileView.as_view(), name='detail_profile'),
    path('update_profile/<str:pk>/<str:slug>', UpdateProfileView.as_view(), name='update_profile'),
    path('create_value/', CreateValueView.as_view(), name='create_value'),
]
