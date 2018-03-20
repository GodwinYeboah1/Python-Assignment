from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
# Create your views here.

def index(request):
    
    print User.objects.all()
    return render(request,'fakeUserForm_app/index.html')

def register(request):
    response =User.objects.register(
        name=request.POST['username'],
        allias=request.POST['allias'],
        email=request.POST['email'],
        password= request.POST['password'],
        confirm_password = request.POST['confirm_password'])

    # if response['valid']:
    #     messages.add_message(request,messages.SUCCESS)

    # if len(response['errors']) >1:
    #     return render(request,'fakeUserForm_app/index.html',{'errors': response['errors']})

    
    return redirect('/')

def login(request):
    response =User.objects.login(
    email=request.POST['email'],
    password= request.POST['password'],
    )
    

    print request.POST
    return redirect('/')
