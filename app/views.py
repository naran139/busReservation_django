from datetime import datetime
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Bus,Location,Schedule,Booking
from django.db.models import Q
from .forms import bookingForms
# from django.contrib.auth.decorators import login_required



# Create your views here.
context={}

def index(request):
    locations = Location.objects.all()
    return render(request,'index.html',{'locations':locations})

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



# def bus(request):
#     buses =Bus.objects.all()
#     return render(request,'bus.html',{'buses':buses})

def bus(request):
    if request.method == 'POST':
        date = datetime.strptime(request.POST['date'],"%Y-%m-%d").date()
        year = date.strftime('%Y')
        month = date.strftime('%m')
        day = date.strftime('%d')
        depart = Location.objects.get(id = request.POST['depart'])
        destination = Location.objects.get(id = request.POST['destination'])
        schedules = Schedule.objects.filter(Q(status=1) & Q(schedule__year = year)& Q(schedule__month = month) & Q(schedule__day = day) & Q(depart= depart )& Q(destination= destination)).all()
        context['schedules']=schedules
        context['data']={'date':date,'depart':depart,'destination':destination}
        return render(request,'bus.html',context)



    return render(request,'bus.html',context)



# @login_required(login_url="/login/")
def bookingForm(request,schedPk=None):
    if not schedPk is None:
        schedule = Schedule.objects.get(code = schedPk)
    fn = bookingForms(initial={'fare':schedule.fare})
    data = {'form': fn, 'schedule': schedule}
    return render(request,'bookings.html',data)


def save_book(request,schedPk=None):
    if not schedPk is None:
        schedule= Schedule.objects.get(code=schedPk)
    if request.method =='POST':
        name = request.POST.get('name')       
        seats = request.POST.get('seats')
        # fare = request.POST.get('fare')       
        data = Booking(name =name ,seats= seats, schedule=schedule)
        data.save()
        return HttpResponse("Successful")
    


    return HttpResponse("Successful")