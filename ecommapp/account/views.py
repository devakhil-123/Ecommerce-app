from django.shortcuts import render,redirect
from django.views import View
from django.urls import reverse_lazy
from .forms import RegForm,LogForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.generic import CreateView,FormView,TemplateView
# Create your views here.


class LandingView(TemplateView):
    template_name="landing.html"


# class LoginView(View):
#     def get(self,request,*args,**kwargs):
#         form=LogForm()
#         return render(request,"login.html",{"form":form})
#     def post(self,request,*args,**kwargs):
#         form_data=LogForm(data=request.POST)
#         if form_data.is_valid():
#             uname=form_data.cleaned_data.get('username')
#             pswd=form_data.cleaned_data.get('password')
#             user=authenticate(request,username=uname,password=pswd)
#             if user:
#                 login(request,user)
#                 messages.success(request,"sign in sucess!!")
#                 return redirect('landing')
                
#             else:
#                 return redirect('uhome')
#         else:
#             return render(request,"login.html",{"form":form_data})

class LoginView(FormView):
    template_name="login.html"
    form_class=LogForm()
    def post(self,request,*args,**kwargs):
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get('username')
            pswd=form_data.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                messages.success(request,"sign in sucess!!")
                return redirect('uhome')
                
            else:
                return redirect('uhome')
        else:
            return render(request,"login.html",{"form":form_data})
        


# class RegView(View):
#     def get(self,request):
#         form=RegForm()
#         return render(request,"reg.html",{"form":form})

#     def post(self,request):
#         form_data=RegForm(data=request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             messages.success(request,"Registration success!!")
#             return redirect('login')
#         messages.error(request,"Validation Failed!")
#         return render(request,"reg.html",{"form":form_data})

class RegView(CreateView):
    form_class=RegForm
    template_name="reg.html"
    success_url=reverse_lazy("login")

class HomeView(View):
    def get(self,request):
        return render(request,"home.html")


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')
   