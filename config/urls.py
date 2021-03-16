from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('portfolioadmin/', admin.site.urls),
    path('', include('portfolio.urls')),
]
