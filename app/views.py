from django.shortcuts import render
from .models import doctorData, studentData, parentData, login, testData
from django.db import connection

def Index(request):
    return render(request, 'Index.html')

def AdminLogin(request):
    return render(request, 'AdminLogin.html')

def UserLogin(request):
    return render(request, 'UserLogin.html')

def AdminNavbar(request):
    return render(request, 'AdminNavbar.html')

def VIEWSTUDENTFORM(request):
    return render(request, 'VIEWSTUDENTFORM.html')

def ViewStudent(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        usn = request.POST.get("usn")
        branch = request.POST.get("branch")
        semester = request.POST.get("semester")
        section = request.POST.get("section")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        print(name,usn,address)
        studentData.objects.create(name=name, usn=usn, branch=branch, semester=semester, section=section, sex=gender, age=age, mobile=mobile, address=address)
        adminViewStudents = studentData.objects.all()
        return render(request, 'ViewStudent.html', {"adminViewStudent":adminViewStudents})
    adminViewStudents = studentData.objects.all()
    return render(request, 'ViewStudent.html', {"adminViewStudent":adminViewStudents})  

def VIEWDOCTORFORM(request):
    return render(request, 'VIEWDOCTORFORM.html')

def ViewDoctor(request):
    if request.method == 'POST':
        udn = request.POST.get("udn")
        name = request.POST.get("name")
        age = request.POST.get("age")
        address = request.POST.get("address")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        speciality = request.POST.get("speciality")
        doctorData.objects.create(udn=udn, name=name, age=age, address=address, sex=gender, mobile=mobile, email=email, speciality=speciality)
        adminViewDocs = doctorData.objects.all()
        return render(request, 'ViewDoctor.html', {"adminViewDoc":adminViewDocs})
    adminViewDocs = doctorData.objects.all()
    return render(request, 'ViewDoctor.html', {"adminViewDoc":adminViewDocs})

def VIEWPARENTFORM(request):
    return render(request, 'VIEWPARENTFORM.html')

def ViewParent(request):
    if request.method == 'POST':
        usn = request.POST.get("usn")
        parent = request.POST.get("parent")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        
        parentData.objects.create(usn=usn, parent=parent, mobile=mobile, email=email, sex=gender)
        adminViewParents = parentData.objects.all()
        return render(request, 'ViewParent.html', {"adminViewParent":adminViewParents})
    adminViewParents = parentData.objects.all()
    return render(request, 'ViewParent.html', {"adminViewParent":adminViewParents})

def UserNavbar(request):
    return render(request, 'UserNavbar.html')

def DoctorLogin(request):
    return render(request, 'DoctorLogin.html')

def DoctorNavbar(request):
    return render(request, 'DoctorNavbar.html')

def HEALTHRECORDFORM(request):
    return render(request, 'HEALTHRECORDFORM.html')

def StudentHealthRecord(request):
    if request.method == 'POST':
        # name = request.POST.get("name")
        # usn = request.POST.get("usn")
        # branch = request.POST.get("branch")
        # semester = request.POST.get("semester")
        # section = request.POST.get("section")
        # gender = "Male"#request.POST.get("gender")
        # age = request.POST.get("speciality")
        # mobile = request.POST.get("mobile")
        # address = request.POST.get("address")
        # docname = request.POST.get("docname")
        usn = request.POST.get("usn")
        test = request.POST.get("test")
        result = request.POST.get("result")
        advice = request.POST.get("advice")
        medicines = request.POST.get("medicines")
        print(test,result,advice,medicines)
        testData.objects.create(usn=usn, test_name=test, result=result, advice=advice, medicines=medicines)
        adminViewTests = testData.objects.all()
        return render(request, 'StudentHealthRecord.html', {"adminViewTest":adminViewTests})
    adminViewTests = testData.objects.all()
    return render(request, 'StudentHealthRecord.html', {"adminViewTest":adminViewTests})

def StudentForm(request):
    return render(request, 'StudentForm.html')
    
def Result(request):
    if request.method == 'POST':
        usn = request.POST.get("usn")
        password = request.POST.get("password")
        # usn1 = login.objects.get(usn=str(usn))
        studViewTests = testData.objects.filter(usn=str(usn))
        return render(request, 'StudentHealthRecord.html', {"adminViewTest" : studViewTests})
            
    return render(request, 'Result.html')

def ViewTests(request):
    return render(request, 'ViewTests.html')


