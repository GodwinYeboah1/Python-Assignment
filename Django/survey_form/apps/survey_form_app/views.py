from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
# this views speaks to the file and involkes the methods bellow

def index(request):

    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] +=1

    date ={
        'current_time': datetime.now()
    }

    return render(request,'survey_form_app/index.html',date)

#  make one method hadle the post 
def process(request):
    
    
    request.session['data'] = request.POST
   
    # this is how you access data from the session remeber session is a dict data type
    print request.session['data']
    print request.session['data']['location']
    return redirect("/result")

def result (request):
    return render(request,'survey_form_app/result.html')