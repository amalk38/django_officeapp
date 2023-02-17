from http.client import HTTPResponse
from xml.dom.minidom import Document
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
import logging


# Create your views here.

def home(request):
    return render(request,'home.html')

def sign_up(request):
    departments=DepartmentModel.objects.all()
    logging.warning('hello') 
    context={'departments':departments}
    return render(request,'sign_up.html',context)



    
def loginpage(request):
    return render(request,'login.html')

    

def DepartmentPage(request):
    return render(request,'adddepartment.html')

def AddDepartment(request):

    if request.method == 'POST':
        departmentname=request.POST['departmentname']
        departmentinfo=request.POST['departmentinfo']
        data = DepartmentModel(Department_Name=departmentname,Department_Info=departmentinfo)
        data.save()
        return redirect('DepartmentPage')








def add_employ_details(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        name=request.POST['email']
        email=request.POST['email']
        dob=request.POST['date']
        age=request.POST['age']
        img=request.FILES.get('img')
        scontact=request.POST['cnumber']
        password=request.POST['password']
        
        select=request.POST['select']
        department=DepartmentModel.objects.get(id=select)

        
        
        

       
        if User.objects.filter(username=name).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                #print("Username already Taken..")
                return redirect('sign_up')
        else:
                user=User.objects.create_user(
                    
                    first_name=fname,
                    last_name=lname,
                    username=name,
                    password=password,
                    email=email)
                    
                user.save()
                Employees=EmployModel(User=user,fname=fname,
                                lname=lname,
                                username=name,
                                dob=dob,
                                Employ_Age=age,
                                Department=department,
                                email=email,
                                phone=scontact,
                                Employ_Photo=img
                            
                                
                               )
                Employees.save()
                send_mail('Your Account has been Successfully Registered',
                'Username: '+Employees.email +'  '+ 
                'password: '+password,
                'amalk425508@gmail.com', 
                [Employees.email],
                fail_silently=False,)
                print(request.POST['password'])

                #messages.info(request, 'SuccessFully completed.......')
                print("*******Successed...*******")
           
        return redirect('loginpage')
    else:
        return render(request,'sign_up.html')



def Employ_login(request):
    if request.method == 'POST':
        global username
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:

            if user.is_staff:
                login(request,user)
                return redirect('admin_home')
            else:
                auth.login(request,user)
                return redirect('user_home')
                







def admin_home(request):
    return render(request,'admin_home.html')


def user_home(request):
     if request.user.is_authenticated:
        current_user = request.user
        name=current_user.username
        ab=EmployModel.objects.filter(username=name)
        return render(request,'user_home.html', {'ab':ab})

def contactus(request):
    return render(request,'contactus.html')



def view_profile(request):
    if request.user.is_authenticated:
        current_user = request.user
        employ=EmployModel.objects.get(User=current_user)
        return render(request,'employ_profile.html', {'student':employ})

def edit_profile(request):
    dep=DepartmentModel.objects.all()
    if request.user.is_authenticated:
        current_user = request.user
        edit=EmployModel.objects.get(User=current_user)
        
        return render(request,'edit.html',{'emp':edit,'Departments':dep})


def deletepage(request):
    if request.user.is_authenticated:
        current_user = request.user
        name=current_user.username
        employ=EmployModel.objects.get(username=name)
    
    employ.delete()
    return redirect('home')


def logout(request):
	auth.logout(request)
	return redirect('home') 


def show_employ_details(request):
    students=EmployModel.objects.all()
    return render(request,'employ_details.html',{'student':students})

def edit_profile(request):
    dep=DepartmentModel.objects.all()
    if request.user.is_authenticated:
        current_user = request.user
        edit=EmployModel.objects.get(User=current_user)
        
        return render(request,'edit.html',{'emp':edit,'Departments':dep})


def edit_student_details(request):
     current_user = request.user
     edit=EmployModel.objects.get(User=current_user)
     if request.method=='POST':
        old=edit.Employ_Photo
        new=request.FILES.get('img')
        if old !=None and new==None:
            edit.Employ_Photo=old
        else:
            edit.Employ_Photo=new
            
       
        edit.fname = request.POST['fname']
        edit.lname=request.POST['lname']
        edit.username=request.POST['name']
        edit.email = request.POST['email']
        edit.phone = request.POST['cnumber']

        edit.dob=request.POST['date']
        edit.Employ_Age=request.POST['age']
        dep=request.POST['select']
        dd=DepartmentModel.objects.get(id=dep)
        edit.Department=dd
        edit.save()
        #print(old)
       # print(request.FILES.get('img'))
        return redirect('view_profile')
     return render(request, 'edit.html')







def task(request,pk):
    employ=EmployModel.objects.get(id=pk)
    return render(request,'task.html',{'employ':employ})



def taskpage(request,pk):
    if request.method == 'POST':
        ur=EmployModel.objects.get(id=pk)
        t_name=request.POST['tname']
        t_desc=request.POST['tdesc']
        s_date=request.POST['sdt']
        e_date=request.POST['edt']
        data=EmployTaskModel(Employ=ur,tname=t_name,tdesc=t_desc,sdate=s_date,edate=e_date)
        data.save()
        return redirect('show_employ_details')


def show_employ_tasks(request):
     if request.user.is_authenticated:
        current_user = request.user
        logging.basicConfig()
        print("*********************************current_user.id") #test
        employ=EmployModel.objects.get(User=current_user)
        tasks=EmployTaskModel.objects.filter(Employ=employ)
        return render(request,'show_task.html', {'tasks':tasks})
   

def show_tasks_for_admin(request,pk):
        logging.basicConfig()
        print("*********************************current_user.id") #test
        employ=EmployModel.objects.get(id=pk)
        tasks=EmployTaskModel.objects.filter(Employ=employ)
        return render(request,'show_employ_task.html', {'tasks':tasks})

def upload_employ_file(request,pk):
     if request.user.is_authenticated:
        current_user = request.user
        employ=EmployModel.objects.get(User=current_user)
        tasks=EmployTaskModel.objects.filter(Employ=employ)
        task=EmployTaskModel.objects.get(id=pk)
        emp_file=request.FILES.get('emp_file')
        task.employ_file=emp_file
        task.save()
        return render(request,'show_task.html', {'tasks':tasks})

def download_emp_file(request,pk):
    task=EmployTaskModel.objects.get(id=pk)
   
    response = HTTPResponse(task.employ_file)
    response['Content-Disposition'] = 'attachment; filename=%s' % 'test'

    return response

def leavepage(request,pk):
    leave=EmployLeaveModel.objects.get(id=pk)
    return render(request,'leave.html',{'employ':leave}) 


def request_leave(request):
     if request.user.is_authenticated:
        current_user = request.user
        employ=EmployModel.objects.get(User=current_user)
        fromDate = request.POST.get('fdate')
        toDate = request.POST.get('tdate')
        reason = request.POST.get('reason')
        status = "PENDING"
        leaveModel = EmployLeaveModel(Employ = employ,from_date=fromDate,to_date=toDate,leave_status =status,reason=reason)
        leaveModel.save()
        return redirect('leave_list')

def emp_leave_page(request):
    return render(request,'leave.html')

def emp_leave_list_page(request):
    if request.user.is_authenticated:
        current_user = request.user
        employ=EmployModel.objects.get(User=current_user)
        leaves=EmployLeaveModel.objects.filter(Employ=employ).order_by('-id')
        return render(request,'show_employ_leaves.html', {'leaves':leaves}) 

def emp_leave_list_page_amdin(request):
    leaves=EmployLeaveModel.objects.all().order_by('-id')
    return render(request,'show_employ_leaves_admin.html', {'leaves':leaves})
    
def admin_update_leave(request):
    leaveId= request.POST.get('leaveId')
    status = request.POST.get('leaveStatus')
    comment = request.POST.get('comment')
    # for key, value in request.POST.items():
    
    leave=EmployLeaveModel.objects.get(id=leaveId)
    # print("*********************************leave ",comment)
    leave.leave_status = status
    leave.admin_comments = comment
    leave.save()
    return redirect('leave_list_admin')




 