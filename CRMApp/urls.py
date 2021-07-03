from django.urls import path
from .views import AccountCreateView,SigninView,IndexView,SignOutView,json
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
urlpatterns=[
    path("",IndexView.as_view(),name="index"),
    path("register",AccountCreateView.as_view(),name="register"),
    path("login",SigninView.as_view(),name="login"),
    path('home', login_required(TemplateView.as_view(template_name="home.html")), name="home"),
    path('logout',SignOutView.as_view(),name="logout"),
    path("json",view.json,name="json")
]