from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from onlineapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.home,name='home'),

    url(r'^AdminLogin/',views.AdminLogin,name='AdminLogin'),
    url(r'^AdminRegister/',views.AdminRegister,name='AdminRegister'),
    url(r'^AdminDashBoard/',views.AdminDashBoard,name='AdminDashBoard'),
    url(r'^AdminForgot_PW/',views.AdminForgot_PW,name='AdminForgot_PW'),


    url(r'^StudentLogin/',views.StudentLogin,name='StudentLogin'),
    url(r'^StudentForgot_PW/',views.StudentForgot_PW,name='StudentForgot_PW'),
    url(r'^StudentRegister/',views.StudentRegister,name='StudentRegister'),
    url(r'^StudentDashBoard/',views.StudentDashBoard,name='StudentDashBoard'),

    url(r'^ExamDetails/',views.ExamDetails,name='ExamDetails'),
    url(r'^test/',views.test,name='test'),
]
