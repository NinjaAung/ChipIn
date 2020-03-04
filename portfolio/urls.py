from django.urls import include, path
from portfolio.views import PortfolioView, CauseDetailView

urlpatterns = [
    path('', PortfolioView.as_view(), name='portfolio'),
    path('accounts/', include('accounts.urls')),
    path('detail/<int:pk>', CauseDetailView.as_view(), name='cause_detail'),
]



