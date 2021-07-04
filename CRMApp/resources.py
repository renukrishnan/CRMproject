from import_export import resources
from CRMApp.models import MyUser,Customer,Item

class UserResource(resources.ModelResource):
    class Meta:
        model=MyUser
        fields="__all__"
class CustomerResource(resources.ModelResource):
    class Meta:
        model=Customer
        fields="__all__"
class ItemResource(resources.ModelResource):
    class Meta:
        model=Item
        feilds="__all__"