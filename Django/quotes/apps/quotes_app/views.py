from django.shortcuts import render, redirect
from .models import User, UserManager, Quote, Favorite
from django.contrib import messages

# Create your views here.
def index(request):
    print "i am in the index method"
    return render(request,'quotes_app/index.html') 

def validate(request):
    if  request.method =="POST":
        print "i am in the validate method"
        print request.POST
            
        # this is how you create a user in the data base with this create function
        response = User.objects.register(
    
            userName = request.POST['userName'],
            alias = request.POST['alias'],
            email = request.POST['email'],
            password = request.POST['password'],
            confirm_password = request.POST['confirm_password'],
            date_of_birth = request.POST['date_of_birth']
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
    response = User.objects.login(
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
    user = User.objects.get(id=request.session["user_id"])
    quotes = Quote.objects.all()
    print "yoooooo", Quote.postedBy

    content = {
        'user': user,

        'quotes': quotes

    }
    print "getting my comments", request.POST

    return render(request, 'quotes_app/quotes.html',content)

def add_quotes(request):
    
    quotes_data = Quote.objects.create(

        postedBy_id = request.session['user_id'],
        quote = request.POST['comment'],
        quotedBy = request.POST['quotedBy']
        # favorites = request.POST[]
    );
    print "checking 123", quotes_data.quote
    return redirect("/quotes")

def user(request,id):
    user = User.objects.get(id=id)
    quotes = Quote.objects.all()
    quotes = Quote.objects.get(id=Quote.id)
    content = {
        'user': user,
        'user_data':  quotes
    
    }
    print "let this work"

    return render(request, 'quotes_app/user.html',content)