from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.

from CRMApp.models import MyUser,Customer,Item

class UserResource(resources.ModelResource):
    class Meta:
        model=MyUser
        fields=("firstname","lastname","email")
class CustomerResource(resources.ModelResource):
    class Meta:
        model=Customer
        fields=("fromGstin","fromTrdName","fromplace")
class ItemResource(resources.ModelResource):
    class Meta:
        model=Item
        feilds=("productName","productDesc")

class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource
    pass
class CustomerAdmin(ImportExportModelAdmin):
    resource_class = CustomerResource
    pass
class ItemAdmin(ImportExportModelAdmin):
    resource_class = ItemResource
    pass

admin.site.register(MyUser)
admin.site.register(Customer)
admin.site.register(Item)