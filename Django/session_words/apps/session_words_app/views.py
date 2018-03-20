from django.shortcuts import render, redirect
from datetime import datetime
# Create your views here.
def index(request):
    time = {
        "time": " - added on " + str(datetime.now())
    }




    
    return render(request, 'session_words_app/index.html', time)

def process(request):
    #  THE DATA 
    request.session['POST'] = request.POST
    if 'data' not in request.session:
        request.session['data'] = []

    print request.session['data']

    # request.session['data']= request.POST
    request.session['data'].append(request.session['POST'])


    print request.POST
    return redirect("/")
def logout(request):
    request.session.clear()

    return redirect("/")