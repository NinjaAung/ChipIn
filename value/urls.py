from django.urls import path
from value.views import CreateValueView


urlpatterns = [
    path('create_value/', CreateValueView.as_view(), name='create_value'),
]