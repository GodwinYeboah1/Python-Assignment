from django.shortcuts import render, redirect
from random import randint

# Create your views here.
def index(request):
 
    if 'gold' not in request.session:
        request.session['gold'] = 0 
    return render(request,'ninja_gold_app/index.html')

def process(request):
# if the method is a post 
    
    if request.method == "POST":

        request.session['gold_found_farm'] = randint(10,21)
        request.session['gold']+= request.session['gold_found_farm']
    
    
        request.session['cave'] = request.POST['cave']
        request.session['cave'] = randint(10,21)
        request.session['gold']+= request.session['cave']

    if request.method == "POST":
        request.session['house'] = request.POST['house']
        request.session['house'] = randint(10,21)
        request.session['gold']+= request.session['house']

    if request.method == "POST":
        request.session['casino'] = request.POST['casino']
        request.session['casino'] = randint(10,21)
        request.session['gold']+= request.session['casino']

    # if request.method == "POST":
    #     request.session['gold_found_farm'] = randint(10,21)
    #     request.session['gold']+= request.session['gold_found_farm']

    # # if request.form['cave'] == "POST":
    #     request.session['cave'] = randint(5,10)
    #     request.session['gold']+= request.session['cave']
 
        return redirect('/')

def reset(request):
    request.session.clear()
    return redirect("/")