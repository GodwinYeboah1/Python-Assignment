from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

# import my User class so i can use it in my views
from .models import User, UserManager
# Create your views here.
def index(request):
    print "in the index"
    # passing 
    # pass all user in the data
    context = {
        'users': User.objects.all(),
    }

    return render(request, 'semi_Restful_app/index.html', context)

def new(request):
    print "in the new method"
    return render(request, 'semi_Restful_app/add_user.html')


#  you want your validtion down in a different method different
# never want to render a POST
def create(request):
    print "in the create function"
    if request.method == 'POST':
        print "This is a post data"

    # validate user 
# passing the request.POST  in the method that i created in the UserManager class
# if errors exist
        errors = User.objects.validate(request.POST)


# passing the request.POST in the moethod that i created in the User manager class
# if no errors  create user
        user = User.objects.create_user(request.POST)

    # redirect user to show page after creating user
    # we are passing this kwargs keyword to the show method 
        return redirect(reverse('show_user', kwargs={'id': user.id}))


    return redirect(reverse('new_user'))

#  passing the kwargs  key to show function bellow so it can aspect it
#  show the data that we have beening passing though
def show(request, id):
    # get user id so we can access the data, because id is specfic to each user so we do that by using the get() method
    user = User.objects.get(id=id)

    print "this is in the views", user
# stores  all the info in this key word 'data'
    context = {
        # DATA IS THE KEYWORD YOUR ARE GOING TO USE IN TEMPLATE FOLDER FOR SHOW HTML PAGE
        'data': user,
    }

# we pass the dict in the render function so we can pass our data in the html file
    return render(request, 'semi_Restful_app/show.html', context)

def delete(request, id):
    delete = User.objectds.id(id=id)
    delete.delete()
    return redirect('show_user')


    