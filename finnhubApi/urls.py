from django.urls import path
from finnhubApi.views import CompanyProfile, CompanyRecommendation, CompanySocialSentiment

urlpatterns = [
    path('profile/<str:company_name>/', CompanyProfile.as_view()),
    path('recommendation/<str:company_name>/<str:min_date>/<str:max_date>/', CompanyRecommendation.as_view()),
    path('social-sentiment/<str:company_name>/<str:min_date>/<str:max_date>/', CompanySocialSentiment.as_view()),
]