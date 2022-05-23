from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
import finnhub
from bigFinance.settings import FINNHUB_API_KEY, FINNHUB_SANDBOX_API_KEY


class CompanyProfile(APIView):  # request only one time
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None, *args, **kwargs):
        finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
        company_name = self.kwargs['company_name']
        response = finnhub_client.company_profile2(symbol=company_name)
        return Response(response, status=status.HTTP_200_OK)


class CompanyQuote(APIView):  # request every-day at 11pm
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None, *args, **kwargs):
        finnhub_client = finnhub.Client(api_key=FINNHUB_SANDBOX_API_KEY)
        company_name = self.kwargs['company_name']
        response = finnhub_client.quote(symbol=company_name)
        response_processed = {
            'company': self.kwargs['company_name'],
            'current_price': response['c'],
            'change': response['d'],
            'percent change': response['dp'],
            'high price of the day': response['h'],
            'low price of the day': response['l'],
            'open price of the day': response['o'],
            'previous close price': response['pc']
        }
        return Response(response_processed, status=status.HTTP_200_OK)


class CompanyRecommendation(APIView):  # request the 2 of each month
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None, *args, **kwargs):
        finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
        company_name = self.kwargs['company_name']
        response = finnhub_client.recommendation_trends(symbol=company_name)
        return Response(response, status=status.HTTP_200_OK)


class CompanySocialSentiment(APIView):  # request every hour
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None, *args, **kwargs):
        finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
        company_name = self.kwargs['company_name']
        response = finnhub_client.stock_social_sentiment(symbol=company_name)
        return Response(response, status=status.HTTP_200_OK)


class MarketNews(APIView):  # request every day at 11 pm
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None, *args, **kwargs):
        finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
        news_category = self.kwargs['news_category']
        response = finnhub_client.general_news(news_category, min_id=0)
        return Response(response, status=status.HTTP_200_OK)