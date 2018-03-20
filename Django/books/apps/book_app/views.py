from django.shortcuts import render
from ..user_app.models import User
from django.contrib import messages

# Create your views here.
def books(request):
    # dont forget the request, " folder name/file name"
    user = User.objects.get(id = request.session["user_id"])
    all_user = User.objects.all()
    temp = {
        'user': user,
        "all_user" : all_user
    }
   
    return render(request, "book_app/index.html", temp)

def add_book(request):
    # dont forget the request, " folder name/file name"
    if 'user' not in request.session:
        messages.add_message(request, messages.SUCCESS, 'welcome to the site ')
        # hold the current user in  session  this is how you know if the person is still long in
        request.session["user_id"] = response["user"].id

    return render(request, "book_app/add.html")

def book_reviews(request):

    return render(request, "book_app/")