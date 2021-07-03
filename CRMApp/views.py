from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .forms import AccountCreationForm,LoginForm
from .models import MyUser,Customer,Item
from django.views.generic import CreateView,TemplateView
from django.http import JsonResponse
import json

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"
    context={}
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.context)
class AccountCreateView(CreateView):
    model=MyUser
    form_class=AccountCreationForm
    template_name="registration.html"
    success_url=reverse_lazy("login.html")

class SigninView(TemplateView):
    model=MyUser
    form_class=LoginForm
    template_name ="login.html"
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                print("Success")
                login(request,user)
                return redirect("home")
            else:
                print("Fail")
            return render(request,self.template_name,self.context)

class SignOutView(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")

def Json(request):
    cdata=list(Customer.objects.values())
    idata=list(Item.objects.values())
    return JsonResponse(cdata,safe=False)
