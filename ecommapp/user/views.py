from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView,DeleteView
from account.models import Products,Cart,Review,Orders
from django.urls import reverse_lazy
from django.contrib import messages
from typing import Any
from django.http import HttpRequest,HttpResponse
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


def signin_required(fn):
        def inner(request,*args,**kwargs):
                 if request.user.is_authenticated:
                        return fn(request,*args,**kwargs)
                 else:
                        messages.error(request,"Please Login First!!")
                        return redirect('log')
        return inner
                        
dec=[signin_required,never_cache]      

@method_decorator(dec,name="dispatch")
class UserHomeView(TemplateView):
        template_name="uhome.html"


@method_decorator(signin_required,name="dispatch")

class UhomeView(TemplateView):
        template_name="uhome.html"


@method_decorator(dec,name="dispatch")
class ProductView(ListView):
        template_name="products.html"
        queryset=Products.objects.all()
        context_object_name="products"
        def get_context_data(self,**kwargs):
                res=Products.objects.filter(categories=self.kwargs.get('cat'))
                print(res)
                print(self.kwargs)
                return {"products":res}
                

@method_decorator(dec,name="dispatch")
class DetailsView(DetailView):
        template_name="details.html"
        queryset=Products.objects.all()
        pk_url_kwarg='pid'
        context_object_name="product"
        def get_context_data(self, **kwargs:any):
                context=super().get_context_data(**kwargs)
                pid=self.kwargs.get('pid')
                product=Products.objects.get(id=pid)
                rev=Review.objects.filter(product=product)
                context["reviews"]=rev
                # print(context)
                return context
dec
def addtocart(request,*args,**kwargs):
        pid=kwargs.get('pid')
        pro=Products.objects.get(id=pid)
        user=request.user
        Cart.objects.create(product=pro,user=user,status='Added')
        return redirect('uhome')

@method_decorator(dec,name="dispatch")
class CartView(ListView):
        template_name="cartlist.html"
        queryset=Cart.objects.all()
        context_object_name="cart"

        def get_queryset(self):
                res=super().get_queryset()
                res=res.filter(user=self.request.user,status='Added')
                return res

@method_decorator(signin_required,name="dispatch")
class CartItemDeleteView(DeleteView):
        model=Cart
        success_url=reverse_lazy('cart')
        template_name="deletecart.html"
        pk_url_kwarg="cid"

@signin_required
def addreview(request,**kwargs):
        review=request.POST.get('rev')
        product_id=kwargs.get('pid')
        product=Products.objects.get(id=product_id)
        user=request.user
        print(review,product_id)
        Review.objects.create(review=review,user=user,product=product)
        messages.success(request,"Review added")
        return redirect('uhome')

@method_decorator(signin_required,name="dispatch")
class PlaceorderView(TemplateView):
    template_name="placeorder.html"
    def post(self,request,*args,**kwargs):
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        cid=kwargs.get('cid')
        cart=Cart.objects.get(id=cid)
        product=cart.product
        user=request.user
        Orders.objects.create(product=product,user=user,address=address,phone=phone)
        cart.status="Order Placed"
        cart.save()
        messages.success(request,"Order Placed Successfully")
        return redirect('uhome')
    
@method_decorator(signin_required,name="dispatch")
class OrderslistView(ListView):
    template_name="orders.html"
    queryset=Orders.objects.all()
    context_object_name="orders"
    

    def get_queryset(self):
        queryset= super().get_queryset()
        queryset=queryset.filter(user=self.request.user)
        return queryset


@signin_required
def cancelorderView(request,**kwargs):
        oid=kwargs.get('oid')
        order=orders.objects.get(id=oid)
        order.order_status="Cancelled"
        order.save()
        #mail service
        to_mail=request.user.email
        msg=f"Order for the product {order.product.title} is cancelled successfully!!check ypur ecommerce account for more details"
        from_mail="devakhinbr@gmail.com"
        subject="Order cancellation confirmation"
        send_mail(subject,msg,from_mail,{to_mail})
        return redirect('order')
