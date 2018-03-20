from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    print "Got to the index page"
    content = {
        'name': 'placeholder for name',
        'email': 'placeholder for  email',
    }


    return render(request,'main_app/index.html', content)

def create(request):
    print "Got your request", request.POST
    request.session['name'] =  request.POST['name']
    request.session['email']= request.POST['email']
    return redirect('/')
