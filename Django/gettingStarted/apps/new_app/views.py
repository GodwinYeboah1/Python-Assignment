from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request,'new_app/index.html')

def create(request):
    print " new User", request.POST     
    print "in the post function"
    request.session['name'] = request.POST['name'],
    request.session['email'] = request.POST['email'],
    request.session['password'] = request.POST['password'],
    return redirect('/show')

def show(request):
    print "in the show function"
    content ={
        'name': request.session['name'],
        'email': request.session['email'],
        'password': request.session['password'],
    }
    return render(request, 'new_app/show.html',content )
def update(request):
    print "in the update function"
    request.session['name'] = request.POST['name'],
    request.session['email'] = request.POST['email'],
    request.session['password'] = request.POST['password'],
    redirect('/show')