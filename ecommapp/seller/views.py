from django.shortcuts import render
from restframework.viewsets import ModelViewSet
from account.models import Products
from .serializers import Productser

# Create your views here.

class SellerModelViewSet(ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=SellerModelSerializer    