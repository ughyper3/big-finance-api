from django.urls import path
from stockDataApi.views import CompanyQuote, CompanyIntradayQuote, CompanyEndOfDayQuote, CompanyNews

urlpatterns = [
    path('quote/<str:company_name>/', CompanyQuote.as_view()),
    path('intraday/<str:company_name>/', CompanyIntradayQuote.as_view()),
    path('end-of-day/<str:company_name>/', CompanyEndOfDayQuote.as_view()),
    path('news/<str:company_name>/', CompanyNews.as_view())
]