from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from myapp.models import Student
from myapp.forms import StudentForm

def home(request):
    return render(request,'apps/home.html')

def about(request):
    return render(request,'apps/about.html')

def read(request):
    stud=Student.objects.all()
    return render(request,'apps/result.html',{'s':stud})

def insert(request):
    form=StudentForm()
    form_class=StudentForm
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'apps/insert.html',{'form':form})

def delete(request,id):
    s=Student.objects.get(id=id)
    s.delete()
    return redirect('/read')

def update(request,id):
    Stud=Student.objects.get(id=id)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=Stud)
        if form.is_valid():
            form.save()
        return redirect('/read')
    return render(request,'apps/update.html',{'s':Stud})

def index(request):
    return render(request,'apps/index.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have Logged in")
            return redirect('/read')
        else:
            messages.success(request,'There was an error Logging In...')
            return redirect('/login')
    else:
        return render(request,'apps/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,'You Have Logged Out...')
    return redirect('/login')
