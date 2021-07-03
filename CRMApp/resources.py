from import_export import resources
from CRMApp.models import MyUser,Customer,Item

class MemberResource(resources.ModelResource):
    class Meta:
        model=MyUser,Customer,Item