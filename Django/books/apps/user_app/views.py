from django.shortcuts import render, redirect
# I need to having access to the database so i need talk to the files that have access which is the models.py
# instead of import Model we need to import User which i have created in the models.py This is consider a table
# import the class that i created User (check model.py to see the table i created)
from .models import User

# importing message to display message on our html page for that session 
from django.contrib import messages


# Create your views here.
# make your view.py only  the routes do not add logic in here
def index(request):
    # this will print all the user that is saved in the database the classname.object.all() 
    print User.objects.all()
    return render(request, "user_app/index.html")

def register(request):

    print request.POST

    # this is how you create a user in the data base with this create function
    response = User.objects.register(
        name = request.POST['name'],
        allias = request.POST['allias'],
        email = request.POST['email'],
        password = request.POST['password'],
        confirm_password = request.POST['confirm_password']
    )

    if response["valid"]:
        messages.add_message(request, messages.SUCCESS, 'Welcome to the site!')
        request.session["user_id"] = response["user"].id
        return redirect('/books')
    else:
        #  i need to for loop to display error  (messege varibale)
        for error_message in response['errors']:
            messages.add_message(request, messages.ERROR, error_message)

    return redirect('/')

# ---------------------------------------------------



# --------------------------------------------------

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