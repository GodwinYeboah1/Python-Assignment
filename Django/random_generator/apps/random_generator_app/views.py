from django.shortcuts import render , redirect
from django.utils.crypto import get_random_string


# Create your views here.
# create your route/ create your urls dowm below
def home(request):
    rand_word ={
        'new_word': get_random_string(length=14)
    }
    return render(request,'random_generator_app/index.html',rand_word)

def generator_random(request):
    # if this is not in session create it and set it to zero
    if  'counter' not in request.session:
        request.session['counter'] =0
    request.session['counter']+=1
    # redirect to the index
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
    