# polls/urls.py
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
    # Add more URL patterns for the polls app as needed
]
