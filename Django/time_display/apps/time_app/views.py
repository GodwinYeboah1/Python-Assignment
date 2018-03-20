from django.shortcuts import render
from time import gmtime, strftime
from datetime import datetime

# Create your views here.
# this is how you rener a page
def index(request):
    # only thing that the client side has access to is the key in the context

    context = {
                "time": strftime("%I:%M %p", gmtime()),
                "date": strftime("%b %m, %y", gmtime()),
                "current": datetime.now(),
             }   

    # can not add two dictinoary in the render
    tryme = {
        "newResponse": "this going to be on the page"
    }

    return render(request,'time_app/index.html',context)

