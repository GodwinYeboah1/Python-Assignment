from django.shortcuts import render
from ..user_app.models import User
from .models import Quote_by

# Create your views here.
def quotes(request):

    user = User.objects.get(id = request.session["user_id"])
    all_user = User.objects.all()
    temp = {
        'user': user,
        "all_user" : all_user
    }
    print Quote_by.objects.all()

    return render(request,'quotes_app/quotes.html', temp)

def check_quote(request):
    request.session['quote_by']= request.POST['quote_by']
    request.session['messages']= request.POST['messages']
    response = {
        "valid" : True,
        'errors': [],
    }

    response = Quote_by.objects.create(
        quote_by = request.POST['quote_by'],
        messages = request.POST['messages'],
    )



    return render(request,'quotes_app/quotes.html', response)