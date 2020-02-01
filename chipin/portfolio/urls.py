from django.urls import path
from portfolio.views import PortfolioView, CauseDetailView

urlpatterns = [
    path('', PortfolioView.as_view(), name='portfolio'),
    path('detail/<int:pk>', CauseDetailView.as_view(), name='cause_detail'),
]



