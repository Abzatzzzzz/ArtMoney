from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('category/<str:slug>', category, name='category',)
]