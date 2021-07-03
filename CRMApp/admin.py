from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import MyUser,Customer,Item
admin.site.register(MyUser)
admin.site.register(Customer)
admin.site.register(Item)

class MemberAdmin(ImportExportModelAdmin):
    list_display = ("firstname","username","email","Gstin")
    pass