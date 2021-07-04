from django.urls import path
from .views import AccountCreateView,SigninView,IndexView,SignOutView,user_home,ItemCreateView,ItemDetailView,ItemListView,ItemUpdateView,ItemDeleteView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns=[
    path("",IndexView.as_view(),name="index"),
    path("register",AccountCreateView.as_view(),name="register"),
    path("login",SigninView.as_view(),name="login"),
    path('home', login_required(TemplateView.as_view(template_name="home.html")), name="home"),
    path('logout',SignOutView.as_view(),name="logout"),
    path("json",views.Json,name="json"),
    path("uhome",user_home,name='uhome'),
    path('items',ItemCreateView.as_view(),name="create"),
    path('items/list',ItemListView.as_view(),name="list"),
    path('items/<int:pk>',ItemUpdateView.as_view(),name="update"),
    path('items/detail/<int:pk>',ItemDetailView.as_view(),name="detail"),
    path('items/remove/<int:pk>',ItemDeleteView.as_view(),name="delete")


]