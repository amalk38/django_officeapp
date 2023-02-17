from django.contrib import admin
from officeapp.models import DepartmentModel, EmployModel

# Register your models here.
@admin.register(DepartmentModel)
class DepartmentDetailAdmin(admin.ModelAdmin):
    list_display=('id','Department_Name','Department_Info')

@admin.register(EmployModel)
class EmployDetailAdmin(admin.ModelAdmin):
    list_display=('id','fname','lname','username','Department','Employ_Age','Employ_Photo','email','dob','phone')




