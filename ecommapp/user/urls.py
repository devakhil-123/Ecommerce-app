from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('uhome',UhomeView.as_view(),name='uhome'),
    path('prolist/<str:cat>',ProductView.as_view(),name='pro'),
    path('det/<int:pid>',DetailsView.as_view(),name='det'),
    path('acart/<int:pid>',addtocart,name="addcart"),
    path('clist',CartView.as_view(),name='cart'),
    path('Crtdel/<int:cid>',CartItemDeleteView.as_view(),name='Cartdel'),
    path('arev/<int:pid>',addreview,name='arev'),
    path('porder/<int:cid>',PlaceorderView.as_view(),name='porder'),
    path('orders',OrderslistView.as_view(),name='order'),
    path('corder/<int:oid>',cancelorderView,name='corder')
    


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)