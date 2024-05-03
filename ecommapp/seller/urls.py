from .views import *
from rest_framework.routers import DefaultRouter

r=DefaultRouter()
r.register('svs',SellerModelViewSet,basename='svs')