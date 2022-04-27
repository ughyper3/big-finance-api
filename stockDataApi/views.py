from requests import get
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from bigFinance.settings import STOCK_DATA_API_KEY


class CompanyQuote(APIView):

    def get(self, request, format=None, *args, **kwargs):
        api_key = STOCK_DATA_API_KEY
        company = self.kwargs['company_name']
        url = f'https://api.stockdata.org/v1/data/quote?symbols={company}&api_token={api_key}'
        response = get(url).json()
        return Response(response, status=status.HTTP_200_OK)


class CompanyIntradayQuote(APIView):

    def get(self, request, format=None, *args, **kwargs):
        api_key = STOCK_DATA_API_KEY
        company = self.kwargs['company_name']
        url = f'https://api.stockdata.org/v1/data/intraday?symbols={company}&api_token={api_key}'
        response = get(url).json()
        return Response(response, status=status.HTTP_200_OK)


class CompanyEndOfDayQuote(APIView):

    def get(self, request, format=None, *args, **kwargs):
        api_key = STOCK_DATA_API_KEY
        company = self.kwargs['company_name']
        url = f'https://api.stockdata.org/v1/data/eod?symbols={company}&api_token={api_key}'
        response = get(url).json()
        return Response(response, status=status.HTTP_200_OK)


class CompanyNews(APIView):

    def get(self, request, format=None, *args, **kwargs):
        api_key = STOCK_DATA_API_KEY
        company = self.kwargs['company_name']
        url = f'https://api.stockdata.org/v1/news/all?symbols={company}&api_token={api_key}'
        response = get(url).json()
        return Response(response, status=status.HTTP_200_OK)