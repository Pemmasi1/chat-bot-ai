from django.urls import path
from . import  views

urlpatterns = [
    path('response/', views.bot_response, name='bot_response'),
]