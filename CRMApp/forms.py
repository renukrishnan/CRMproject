from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser,Customer,Item
from django.forms import ModelForm

class AccountCreationForm(UserCreationForm):
    class Meta:
        model=MyUser
        fields=["first_name","last_name","username","email","password1","password2","Gstin","Address1","Address2","Trade_name","place","pincode"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class ItemCreateForm(ModelForm):
    class Meta:
        model=Item
        fields="__all__"

class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields="__all__"