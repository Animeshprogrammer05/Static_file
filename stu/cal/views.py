from django.shortcuts import render

# Create your views here.
import datetime

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is my first Django statement..!,</h1>")

def date_time_view(request):
    date=datetime.datetime.now()
    h=int(date.strftime("%H"))

    if h<12:
        msg="Hello everyone ..! this is goodmorning time..!"

    elif h<16:
        msg = "Hello everyone ..! this is goodafternoon time..!"
    elif h<21:
        msg = "Hello everyone ..! this is goodevening time..!"

    else :
        msg = "Hello everyone ..! this is goodnight time..!"

    my_dict={'date':date,'msg':msg}

    return render(request,'cal/home.html',my_dict)