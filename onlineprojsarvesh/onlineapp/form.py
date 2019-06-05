from django import forms
from django.core import validators
from onlineapp.models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField




Difficulty_Choices = [("--Choices--","--Choices--"),("EASY","easy"),("MEDIUM","medium"),("HARD","hard")]
Exam_Name = [("--Choices--","--Choices--"),("JAVA","java"),("JAVASCRIPT","javascript"),("python","python")]


def NameCheck(Value):
    for i in range(0,len(Value)):
        if(not ((ord(Value[i]) >=97) and (ord(Value[i])<=122))):
            raise forms.ValidationError("All Letters Should Be In Small Letter Format!!!")

def IdCheck(Value):
    for i in range(0,len(Value)):
        if(not ((Value[i].isalpha()) or (Value[i].isnumeric()))):
            raise forms.ValidationError("No Letters Should Be A Special Character!!!")

def PWCheck(Value):
    k=0
    h=0
    for i in range(0,len(Value)):
        if(Value[i].isalpha()):
            k=1
        if(Value[i].isnumeric()):
            h=1
    if(not(k==1 and h==1)):
            raise forms.ValidationError("Should Contain Letters and Numbers Both")

class AdminLogin(forms.Form):
    Login_ID = forms.CharField()
    Password = forms.CharField(widget = forms.PasswordInput)

class AdminRegister(forms.ModelForm):
    Admin_Name = forms.CharField(validators=[NameCheck]),
    Admin_Id = forms.CharField(validators=[IdCheck])
    Password = forms.CharField(widget = forms.PasswordInput,validators=[PWCheck])
    Confirm_PassWord = forms.CharField(widget = forms.PasswordInput)
    Email_ID = forms.EmailField()
    Contact_No = forms.IntegerField()
    Password_Key = forms.CharField()

    class Meta():
        model = AdminDetails
        fields="__all__"

class StudentRegister(forms.ModelForm):
    Student_Name = forms.CharField(validators=[NameCheck]),
    Student_Id = forms.CharField(validators=[IdCheck])
    Password = forms.CharField(widget = forms.PasswordInput,validators=[PWCheck])
    Confirm_PassWord = forms.CharField(widget = forms.PasswordInput)
    Email_ID = forms.EmailField()
    Contact_No = forms.IntegerField()
    Password_Key = forms.CharField()

    class Meta():
        model = StudentDetails
        fields="__all__"


class StudentLogin(forms.Form):
    Login_ID = forms.CharField()
    Password = forms.CharField(widget = forms.PasswordInput)


class StudentForgotPW(forms.Form):
    Login_ID = forms.CharField()
    Email_ID = forms.EmailField()
    Password_Key = forms.CharField()
    NewPassword = forms.CharField(widget = forms.PasswordInput,validators=[PWCheck])
    Confirm_PassWord = forms.CharField(widget = forms.PasswordInput)

class AdminForgotPW(forms.Form):
    Login_ID = forms.CharField()
    Email_ID = forms.EmailField()
    Password_Key = forms.CharField()
    NewPassword = forms.CharField(widget = forms.PasswordInput,validators=[PWCheck])
    Confirm_PassWord = forms.CharField(widget = forms.PasswordInput)

class SelectQuestion(forms.Form):
    ExamName = forms.CharField(widget=forms.Select(choices=Exam_Name))
    Question = forms.CharField()
    Option1 =  forms.CharField()
    Option2 =  forms.CharField()
    Option3 =  forms.CharField()
    Option4 =  forms.CharField()
    Answer =   forms.IntegerField()
    Choose =   forms.CharField(widget=forms.Select(choices=Difficulty_Choices ))

class questions_form(forms.Form):
    language = forms.CharField()
    questio_name = forms.CharField()
    option_1 = forms.CharField()
    option_2 = forms.CharField()
    option_3 = forms.CharField()
    option_4 = forms.CharField()
    currect_answer = forms.CharField()