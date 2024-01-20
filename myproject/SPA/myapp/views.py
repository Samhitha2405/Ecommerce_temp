from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello1(request):
    return HttpResponse("<center>Welcome to SPA Homepage</center>")
def myhome(request):
    return render(request,'myhome.html')
def mydeals(request):
    return render(request,'todaysdeal.html')
def skincare(request):
    return render(request,'skincare.html')
def buynow(request):
    return render(request,'buynow.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
