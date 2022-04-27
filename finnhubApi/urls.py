from django.urls import path
from finnhubApi.views import CompanyProfile, CompanyQuote, MarketNews, CompanyRecommendation, CompanySocialSentiment

urlpatterns = [
    path('profile/<str:company_name>/', CompanyProfile.as_view()),
    path('quote/<str:company_name>/', CompanyQuote.as_view()),
    path('recommendation/<str:company_name>/', CompanyRecommendation.as_view()),
    path('social-sentiment/<str:company_name>/', CompanySocialSentiment.as_view()),
    path('news/<str:news_category>/', MarketNews.as_view())

]