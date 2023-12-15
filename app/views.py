from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout



# Create your views here.


def index(request):
    return render(request,'index.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        if not User.objects.filter(username = username).exists():
            messages.error(request, "Email Doesn't exits")
            return redirect('/login/')
    
        user = authenticate(username = username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/index/')


    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')


        user = User.objects.filter(email = email)

        if user.exists():
            messages.error(request, "Email already exits")
            return redirect('/register/')


        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.error(request, "Username already exits")
            return redirect('/register/')
    

        user = User.objects.create(
            email = email,
            username = username,
            password = password
        )
        user.set_password(password)
        user.save()
        return redirect ('/login/')
    return render(request,'register.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')



def bus(request):
    return render(request,'bus.html')