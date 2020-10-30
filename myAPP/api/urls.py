from django.contrib import admin
from django.urls import path, include

from api import views

urlpatterns = [
    # path('', ),
    path('index', views.index, name='index'),
    path('search', views.search, name='search'),
]