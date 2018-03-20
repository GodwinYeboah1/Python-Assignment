from django.shortcuts import render,redirect
from .models import *
# Create your views here.
# render home page
def home(request):
    # this is how you pass all the data
    # data is just the label
    # courses is the key we used in the client side
    data = {
        'courses': Course.objects.all()
    }

    return render(request, 'course_app/home.html', data)

def add(request):
    
    Course.objects.create(
    name = request.POST['name'],
    description = request.POST['description']
    ) 

    return redirect('/')

def post_info(request, name_id):


    return redirect('/')