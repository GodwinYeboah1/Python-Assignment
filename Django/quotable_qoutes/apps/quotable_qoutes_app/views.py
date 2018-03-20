from django.shortcuts import render, redirect
from .models import registration, registrationManager, quotes, favorites
from django.contrib import messages

# Create your views here.
def index(request):
    print "i am in the index method"
    return render(request,'quotable_qoutes_app/index.html') 

def validate(request):
    if  request.method =="POST":
        print "i am in the validate method"
        print request.POST
            
        # this is how you create a user in the data base with this create function
        response = registration.objects.register(
    
            userName = request.POST['userName'],
            alias = request.POST['alias'],
            email = request.POST['email'],
            password = request.POST['password'],
            confirm_password = request.POST['confirm_password']
        )

        if response["valid"]:
            messages.add_message(request, messages.SUCCESS, 'Welcome to the site!')
            request.session["user_id"] = response["user"].id
            return redirect('/')
        else:
            #  i need to for loop to display error  (messege varibale)
            for error_message in response['errors']:
                messages.add_message(request, messages.ERROR, error_message)
        return redirect('/')

def login(request):
    # this is how you create a login user in the data base with this create function
    response = registration.objects.login(
        email = request.POST['email'],
        password = request.POST['password'],
    )

# validtion check bellow 
    if response["valid"]:
        messages.add_message(request, messages.SUCCESS, 'welcome to the site ')
        # hold the current user in  session  this is how you know if the person is still long in
        request.session["user_id"] = response["user"].id
        # $$$$why this redirect did not work even though it is valid
        return redirect('/quotes')
    else:
        #  i need to for loop to display error  (messege varibale)
        for error_message in response['errors']:
            messages.add_message(request, messages.ERROR, error_message)
            
    return redirect('/')

# ends session
# logout user
def logout(request):
    # clear user in session 
    request.session.clear()

    # redirect it to the index
    return redirect("/")

def quotes(request):

    # i need to pass in object so i can pass in data 
    user = registration.objects.get(id=request.session["user_id"])

    content = {
        'user': user

    }
    print "getting my comments", request.POST

    return render(request, 'quotable_qoutes_app/quotes.html',content)