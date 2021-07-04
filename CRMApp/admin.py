from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.

from CRMApp.models import MyUser,Customer,Item
@admin.register(MyUser)
@admin.register(Customer)
@admin.register(Item)
class UserResource(ImportExportModelAdmin):
    pass
class CustomerResource(ImportExportModelAdmin):
    pass
class ItemResource(ImportExportModelAdmin):
    pass
