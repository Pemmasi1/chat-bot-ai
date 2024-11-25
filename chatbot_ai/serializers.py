from rest_framework import serializers
from .models import BotResponse,Customer

class BotResponseSerializer:
    class Meta:
        model = BotResponse
        fields = ('message')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'email', 
            'phone_number', 
            'address', 
            'city', 
            'state', 
            'country', 
            'zip_code', 
            'date_of_birth', 
            'created_at', 
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']  
