from django.shortcuts import render
from django.http import HttpResponse
from onlineapp.models import *
from django import forms
from onlineapp import form


#Home_Page
def home(request):
    return render(request,'home.html',{})

#Admin_Login
def AdminLogin(request):
    form_var = form.AdminLogin()
    qform = form.questions_form
    if(request.method == "POST"):
        form_var = form.AdminLogin(request.POST)
        if(form_var.is_valid()):
            Login_ID1 = request.POST["Login_ID"]
            Password1 = request.POST["Password"]

            data = AdminDetails.objects.filter(Admin_Id=Login_ID1).all()
            for i in data:
                Admin_Id = i.Admin_Id
                Password = i.Password
                if(Admin_Id == Login_ID1 and Password == Password1):
                    return render(request,"AdminDashBoard.html",{'form':qform})
                else:
                    return HttpResponse("wrong enterd")
        else:
            return HttpResponse("The form fields are not valid")
    return render(request,"AdminLogin.html",{'form':form_var})

#Admin_Register
def AdminRegister(request):
    form_var = form.AdminRegister()
    if(request.method == "POST"):
        form_var = form.AdminRegister(request.POST)

        if(form_var.is_valid()):
            Admin_Name1 = request.POST['Admin_Name']
            Password1 = request.POST['Password']
            Confirm_PassWord1 = request.POST['Confirm_PassWord']
            if(Password1 == Confirm_PassWord1):
                form_var.save(commit = True)
                return render(request,"AdminDashBoard.html",{})
        else:
            return HttpResponse("The form fields are not valid")
    return render(request,"AdminRegister.html",{'form':form_var})


#Student_Login
def StudentLogin(request):
    form_var = form.StudentLogin()
    if(request.method == "POST"):
        form_var = form.StudentLogin(request.POST)
        if(form_var.is_valid()):
            Login_ID1 = request.POST["Login_ID"]
            Password1 = request.POST["Password"]
            data = StudentDetails.objects.filter(Student_Id=Login_ID1).all()
            for i in data:
                Student_Id = i.Student_Id
                Password = i.Password
                if(Student_Id == Login_ID1 and Password == Password1):
                    return StudentDashBoard(request)
                else:
                    return HttpResponse("The LoginID and Password that you entred are wrong")
        else:
            return("The forms fields are not valid")
    return render(request,"StudentLogin.html",{'form':form_var})

#Student_Register
def StudentRegister(request):
    form_var = form.StudentRegister()
    if(request.method == "POST"):
        form_var = form.StudentRegister(request.POST)
        if(form_var.is_valid()):
            Student_Name1 = request.POST['Student_Name']
            Password1 = request.POST['Password']
            Confirm_PassWord1 = request.POST['Confirm_PassWord']
            if(Password1 == Confirm_PassWord1):
                form_var.save(commit = True)
                return render(request,"StudentDashBoard.html",{})
    else:
        return HttpResponse("The form are not Valid")
    return render(request,"StudentRegister.html",{'form':form_var})


#Student_DashBoard
def StudentDashBoard(request):
    return render(request,"StudentDashBoard.html",{})


#Admin_DashBoard
def AdminDashBoard(request):
    form_var = form.SelectQuestion()
    return render(request,"AdminDashBoard.html",{})


#Exam_Details
def ExamDetails(request):
    return render(request,"ExamDetails.html",{})

#test
def test(request):
    return render(request,"test.html",{})



#Forgot_Password_of_Student
def StudentForgot_PW(request):
    form_var = form.StudentForgotPW()
    if(request.method=="POST"):
        form_var = form.StudentForgotPW(request.POST)
        if(form_var.is_valid()):
            Login_ID1 = request.POST['Login_ID']
            Email_ID1 = request.POST['Email_ID']
            Password_Key1 = request.POST['Password_Key']
            Password1 = request.POST['NewPassword']
            Confirm_PassWord1 = request.POST['Confirm_PassWord']
            User_Type1 = request.POST['User_Type']

            if(User_Type1 == "Student"):
                data = StudentDetails.objects.filter(Student_Id=Login_ID1).all()
                for i in data:
                    Student_Id2 = i.Student_Id
                    Email_ID2 = i.Email_ID
                    Password_Key2 =i.Password_Key

                    Student_Name1 = i.Student_Name
                    count = AddEnquiry.objects.filter(Student_Name=Student_Name1).count()

                if((Login_ID1 == Student_Id2 and Email_ID1 == Email_ID2) and (Password1 == Confirm_PassWord1 and Password_Key1 == Password_Key2)):
                    data = StudentDetails.objects.filter(Email_ID = Email_ID1).update(Password=Password1,Confirm_PassWord=Confirm_PassWord1,Password_Key=Password_Key1)

                    return render(request,"StudentDashBoard.html",{'count':count})

    return render(request,"StudentForgotForm.html",{'form':form_var})

#Forgot_Password_of_Admin
def AdminForgot_PW(request):
    form_var = form.AdminForgotPW()
    if(request.method=="POST"):
        form_var = form.AdminForgotPW(request.POST)
        if(form_var.is_valid()):
            Login_ID1 = request.POST['Login_ID']
            Email_ID1 = request.POST['Email_ID']
            Password_Key1 = request.POST['Password_Key']
            Password1 = request.POST['NewPassword']
            Confirm_PassWord1 = request.POST['Confirm_PassWord']
            User_Type1 = request.POST['User_Type']

            if(User_Type1 == "Admin"):
                data = StudentDetails.objects.filter(Admin_Id=Login_ID1).all()
                for i in data:
                    Admin_Id2 = i.Admin_Id
                    Email_ID2 = i.Email_ID
                    Password_Key2 =i.Password_Key

                    Admin_Name1 = i.Admin_Name
                    count = AddEnquiry.objects.filter(Admin_Name=Admin_Name1).count()

                if((Login_ID1 == Admin_Id2 and Email_ID1 == Email_ID2) and (Password1 == Confirm_PassWord1 and Password_Key1 == Password_Key2)):
                    data = AdminDetails.objects.filter(Email_ID = Email_ID1).update(Password=Password1,Confirm_PassWord=Confirm_PassWord1,Password_Key=Password_Key1)

                    return render(request,"AdminDashBoard.html",{'count':count})

    return render(request,"AdminForgotForm.html",{'form':form_var})
