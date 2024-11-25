from django.shortcuts import render
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import BotResponse, Customer
from .serializers import BotResponseSerializer,CustomerSerializer
import logging


@api_view(['GET', 'POST', 'PUT'])
def bot_response(request):
     if request.method == 'GET':
          customer = Customer.objects.all()
          serializer = CustomerSerializer(customer, many=True)
          return Response(serializer.data)
     elif request.method == 'POST':
          serializer = CustomerSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)