from django.urls import path
from .views import *


urlpatterns=[
    path('login',LoginView.as_view(),name='login'),
    path('reg',RegView.as_view(),name='reg'),
    path('home',HomeView.as_view(),name='home'),
    path('logout',LogoutView.as_view(),name='logout')

]