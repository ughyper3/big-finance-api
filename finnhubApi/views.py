from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
import finnhub
from bigFinance.settings import FINNHUB_API_KEY, FINNHUB_SANDBOX_API_KEY


class CompanyProfile(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None, *args, **kwargs):
        finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
        company_name = self.kwargs['company_name']
        response = finnhub_client.company_profile2(symbol=company_name)
        return Response(response, status=status.HTTP_200_OK)


class CompanyQuote(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None, *args, **kwargs):
        finnhub_client = finnhub.Client(api_key=FINNHUB_SANDBOX_API_KEY)
        company_name = self.kwargs['company_name']
        response = finnhub_client.quote(symbol=company_name)
        return Response(response, status=status.HTTP_200_OK)


class CompanyRecommendation(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None, *args, **kwargs):
        finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
        company_name = self.kwargs['company_name']
        response = finnhub_client.recommendation_trends(symbol=company_name)
        return Response(response, status=status.HTTP_200_OK)


class CompanySocialSentiment(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None, *args, **kwargs):
        finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
        company_name = self.kwargs['company_name']
        response = finnhub_client.stock_social_sentiment(symbol=company_name)
        return Response(response, status=status.HTTP_200_OK)


class MarketNews(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None, *args, **kwargs):
        finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
        news_category = self.kwargs['news_category']
        response = finnhub_client.general_news(news_category, min_id=0)
        return Response(response, status=status.HTTP_200_OK)