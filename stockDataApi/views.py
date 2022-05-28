from requests import get
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from bigFinance.settings import STOCK_DATA_API_KEY


class CompanyIntradayQuote(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None, *args, **kwargs):
        api_key = STOCK_DATA_API_KEY
        company = self.kwargs['company_name']
        interval = 'day'
        date_from = self.kwargs['date_from']
        date_to = self.kwargs['date_to']
        url = f'https://api.stockdata.org/v1/data/intraday?symbols={company}' \
              f'&api_token={api_key}' \
              f'&interval={interval}' \
              f'&date_from={date_from}' \
              f'&date_to={date_to}'
        response = get(url).json()['data']
        return Response(response, status=status.HTTP_200_OK)


class CompanyNews(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None, *args, **kwargs):
        api_key = STOCK_DATA_API_KEY
        company = self.kwargs['company_name']
        published_after = self.kwargs['published_after']
        published_before = self.kwargs['published_before']
        url = f'https://api.stockdata.org/v1/news/all?symbols={company}' \
              f'&api_token={api_key}' \
              f'&published_after={published_after}' \
              f'&published_before={published_before}'
        response = get(url).json()['data']
        return Response(response, status=status.HTTP_200_OK)