from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import User, Quote, Favorite

def index(request):
    # print(User.objects.all())
    return render(request, 'project1_app/index.html')

def register(request):
    # print request.POST
    response = User.objects.register(
        name = request.POST["name"],
        alias = request.POST["alias"],
        email = request.POST["email"],
        password = request.POST["password"],
        confirm_password = request.POST["confirm_password"],
        bday = request.POST["bday"],
    )
    print("hello we are here", response)
    if response['valid']:
        messages.add_message(request, messages.SUCCESS, 'Welcome to the site!')
        request.session["user_id"]=response["user"].id
        request.session["name"]=response["user"].name
        return redirect("/quotes")
    else:
        for error_message in response["errors"]:
            messages.add_message(request, messages.ERROR, error_message)
    return redirect("/")
 
def login(request):
    response = User.objects.login(
        email = request.POST["email"],
        password = request.POST["password"]
    )
    if response['valid']:
        messages.add_message(request, messages.SUCCESS, 'Welcome to the site!')
        request.session["user_id"]=response["user"].id
        request.session["name"]=response["user"].name
        return redirect("/quotes")
    else:
        for error_message in response["errors"]:
            messages.add_message(request, messages.ERROR, error_message)

    return redirect("/")

def quotes(request):
    if "user_id" not in request.session:
        return redirect("/")
    otherQuotes=Quote.objects.all()
    userQuotes=User.objects.get(id=request.session["user_id"]).fav_quotes.all()#getting all the users favorite quotes
    for quote in userQuotes:
        otherQuotes=otherQuotes.exclude(id=quote.id) #overwriting the otherQuotes
#move quotes from quoatable quotes to favorites
    data={
        "quotations":otherQuotes,
        "this_user":User.objects.get(id=request.session["user_id"])
    }
   #print User.objects.all()
    return render(request, 'project1_app/quotes.html', data)

def add_quote(request):
    quotation=Quote.objects.create(
        message=request.POST["message"],
        author=request.POST["author"],
        posted_by_id=request.session["user_id"]
    )
    print "***********************"
    print Quote.objects.all()
    return redirect("/quotes")

def add_favorites(request, id):
    this_quote=Quote.objects.get(id=id)#assign all quoates with these id
    this_user=User.objects.get(id=request.session["user_id"])
    #asssign user object that is in session
    this_quote.favoring_users.add(this_user) #adding quotes to favorite list
    
    return redirect("/quotes")

def remove_favorites(request,id):
    this_quote=Quote.objects.get(id=id)#assign all quoates with these id
    this_user=User.objects.get(id=request.session["user_id"])
    #asssign user object that is in session
    this_quote.favoring_users.remove(this_user) #adding quotes to favorite list

def display_posts(request, id):
    data={
        "this_user": User.objects.get(id=id),
        "quotations": Quote.objects.filter(posted_by_id=id)
    }
    return render(request, 'project1_app/postbyuser.html', data)
def logout(request):
    request.session.clear()
    return redirect('/')




