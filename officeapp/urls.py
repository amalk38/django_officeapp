from django.urls import path
from . import views
from django.conf import settings  
from django.conf.urls.static import static 
urlpatterns = [


    path('',views.home,name='home'),
    path('sign_up',views.sign_up,name='sign_up'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('add_employ_details',views.add_employ_details,name='add_employ_details'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('Employ_login',views.Employ_login,name='Employ_login'),
    path('user_home',views.user_home,name='user_home'),
    path('logout',views.logout,name='logout'),
    path('DepartmentPage',views.DepartmentPage,name='DepartmentPage'),
    
    path('AddDepartment',views.AddDepartment,name='AddDepartment'),
    
    path('show_employ_details',views.show_employ_details,name='show_employ_details'),
    path('deletepage',views.deletepage,name='deletepage'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('edit_student_details',views.edit_student_details,name='edit_student_details'),
    path('view_profile',views.view_profile,name='view_profile'),
    
    path('leavepage',views.emp_leave_page,name='leavepage'),
    path('leave_list',views.emp_leave_list_page,name='leave_list'),
    path('Addleave',views.request_leave,name='Addleave'),
    path('leave_list_admin',views.emp_leave_list_page_amdin,name='leave_list_admin'),
    path('leave_update_admin',views.admin_update_leave,name='leave_update_admin'),

    path('contactus',views.contactus,name='contactus'),


    path('task/<int:pk>',views.task,name='task'),
    path('taskpage/<int:pk>',views.taskpage,name='taskpage'),
    path('task_list',views.show_employ_tasks,name='task_list'),
    path('task_list/<int:pk>',views.show_tasks_for_admin,name='task_list_for_admin'),
    path('upload_task_file/<int:pk>',views.upload_employ_file,name='upload_employ_file'),
    path('download_emp_file/<int:pk>',views.download_emp_file,name='download_emp_file'),
    

    



    
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 