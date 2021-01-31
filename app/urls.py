from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.Index, name='Index'),
    path('AdminLogin', views.AdminLogin, name='AdminLogin'),
    path('UserLogin', views.UserLogin, name='UserLogin'),
    path('UserNavbar', views.UserNavbar, name='UserNavbar'),
    path('AdminNavbar', views.AdminNavbar, name='AdminNavbar'),
    path('DoctorLogin', views.DoctorLogin, name='DoctorLogin'),
    path('DoctorNavbar', views.DoctorNavbar, name='DoctorNavbar'),
    path('ViewStudent', views.ViewStudent, name='ViewStudent'),
    path('ViewDoctor', views.ViewDoctor, name='ViewDoctor'),
    path('ViewParent', views.ViewParent, name='ViewParent'),
    path('StudentForm', views.StudentForm, name='StudentForm'),
    path('StudentHealthRecord', views.StudentHealthRecord, name='StudentHealthRecord'),
    path('HEALTHRECORDFORM', views.HEALTHRECORDFORM, name='HEALTHRECORDFORM'),
    path('VIEWDOCTORFORM', views.VIEWDOCTORFORM, name='VIEWDOCTORFORM'),
    path('VIEWPARENTFORM', views.VIEWPARENTFORM, name='VIEWPARENTFORM'),
    path('VIEWSTUDENTFORM', views.VIEWSTUDENTFORM, name='VIEWSTUDENTFORM'),
    path('ViewTests', views.ViewTests, name='ViewTests'),
    path('ViewTests', views.ViewTests, name='ViewTests'),
    path('Result', views.Result, name='Result'),
    #path('users/', include('dbms.urls'))
]