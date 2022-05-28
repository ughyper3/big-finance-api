from django.urls import path
from stockDataApi.views import CompanyIntradayQuote, CompanyNews

urlpatterns = [
    path('intraday/<str:company_name>/<str:date_from>/<str:date_to>/', CompanyIntradayQuote.as_view()),
    path('news/<str:company_name>/<str:published_after>/<str:published_before>/', CompanyNews.as_view())
]