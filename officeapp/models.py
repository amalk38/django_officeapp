
from django.db import models
from django.contrib.auth.models import User,auth



# Create your models here.
class DepartmentModel(models.Model):
    Department_Name=models.CharField(max_length=70)
    Department_Info=models.CharField(max_length=70)


class EmployModel(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    Department=models.ForeignKey(DepartmentModel,on_delete=models.CASCADE,null=True)
    Employ_Age=models.IntegerField()
    Employ_Photo=models.ImageField(null=True,blank=True,upload_to='image/')
    email=models.CharField(max_length=255)
    dob=models.CharField(max_length=255)
    phone=models.IntegerField()


class EmployTaskModel(models.Model):
    Employ=models.ForeignKey(EmployModel,on_delete=models.CASCADE,null=True)
    tname=models.CharField(max_length=200)
    tdesc=models.CharField(max_length=200)
    sdate=models.CharField(max_length=200)
    edate=models.CharField(max_length=200)
    employ_file=models.FileField(null=True,blank=True,upload_to='emp_files/')




class EmployLeaveModel(models.Model):
    Employ=models.ForeignKey(EmployModel,on_delete=models.CASCADE,null=True)
    from_date=models.DateField(null=True)
    to_date=models.DateField(null=True)
    leave_status=models.CharField(max_length=200)
    reason=models.CharField(max_length=200)
    admin_comments=models.CharField(max_length=200)










