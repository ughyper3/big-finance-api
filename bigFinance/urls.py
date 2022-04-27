from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('bigFinanceApi.urls')),
    path('finnhub/api/v1/', include('finnhubApi.urls')),
    path('stockdata/api/v1/', include('stockDataApi.urls'))
]
