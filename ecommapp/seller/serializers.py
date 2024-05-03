from rest_framework import serializers
from account.models import Products



class Productser(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields="__all__"