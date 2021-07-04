from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .forms import AccountCreationForm,LoginForm,ItemCreateForm,CustomerForm
from .models import MyUser,Customer,Item
from django.views.generic import CreateView,TemplateView,ListView,DetailView,UpdateView,DeleteView
from django.http import JsonResponse
from .decorators import loginrequired
from django.http import HttpResponse
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
    success_url=reverse_lazy("login")

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
                return redirect("uhome")
            else:
                print("Fail")
            return render(request,self.template_name,self.context)

class SignOutView(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")

def Json(request):
    cdata=list(Customer.objects.values())
    idata=list(Item.objects.values())
    data=cdata+idata
    return JsonResponse(data,safe=False)

@loginrequired
def user_home(request,*args,**kwargs):
        items=Item.objects.all()
        context={
            "items":items
        }
        return render(request,"home.html",context)

class GetObjectMixin:
    def get_object(self,id):
        return self.model.objects.get(id=id)

class ItemCreateView(CreateView):
    model=Item
    form_class=ItemCreateForm
    template_name = "itemcreate.html"
    success_url= reverse_lazy("list")

class ItemListView(ListView):
    model=Item
    template_name = "listitem.html"
    context_object_name = "items"

class ItemDetailView(DetailView):
    model=Item
    template_name = "itemdetail.html"
    context_object_name="item"

class ItemUpdateView(UpdateView):
    template_name = "updateitem.html"
    form_class=ItemCreateForm
    model=Item
    success_url=reverse_lazy("list")

class ItemDeleteView(DeleteView):
    model = Item
    template_name = "delete.html" # django view expecting a template here to confirm delete. thats y template name and success url is given here
    success_url= reverse_lazy("list")

class PlaceOrderView(TemplateView):
    model = Customer
    template_name = "placeorder.html"
    form_class=CustomerForm
    success_url= reverse_lazy("ordersuccess")
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, self.context)
