from datetime import datetime

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
import finnhub
from bigFinance.settings import FINNHUB_API_KEY


class CompanyProfile(APIView):  # request only one time
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None, *args, **kwargs):
        finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
        company_name = self.kwargs['company_name']
        response = finnhub_client.company_profile2(symbol=company_name)
        return Response(response, status=status.HTTP_200_OK)


class CompanyRecommendation(APIView):  # request the 2 of each month
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None, *args, **kwargs):
        finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
        company_name = self.kwargs['company_name']
        min_date = self.kwargs['min_date']
        max_date = self.kwargs['max_date']
        response = finnhub_client.recommendation_trends(symbol=company_name)
        list_of_responses = []
        for response in response:
            if datetime.strptime(min_date, '%Y-%m-%d') <= datetime.strptime(response['period'], '%Y-%m-%d') <= datetime.strptime(max_date, '%Y-%m-%d'):
                list_of_responses.append(response)
        return Response(list_of_responses, status=status.HTTP_200_OK)


class CompanySocialSentiment(APIView):  # request every hour
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None, *args, **kwargs):
        finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
        company_name = self.kwargs['company_name']
        min_date = self.kwargs['min_date']
        max_date = self.kwargs['max_date']
        response = finnhub_client.stock_social_sentiment(symbol=company_name, _from=min_date, to=max_date)
        tweets = response['twitter'].copy()
        reddits = response['reddit'].copy()
        processed_response = []
        for tweet in tweets:
            tweet['media'] = 'twitter'
            tweet['company'] = company_name
            processed_response.append(tweet)
        for reddit in reddits:
            reddit['media'] = 'reddit'
            reddit['company'] = company_name
            processed_response.append(reddit)
        return Response(processed_response, status=status.HTTP_200_OK)