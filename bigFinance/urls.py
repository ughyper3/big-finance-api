from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from bigFinanceApi.views import Documentation

urlpatterns = [
    path('', RedirectView.as_view(url='documentation/', permanent=False)),
    path('documentation/', Documentation.as_view(), name='documentation'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('bigFinanceApi.urls')),
    path('finnhub/api/v1/', include('finnhubApi.urls')),
    path('stockdata/api/v1/', include('stockDataApi.urls'))
]
