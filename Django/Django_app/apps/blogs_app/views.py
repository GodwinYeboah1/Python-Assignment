from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
#   method are the new pages 


def index(request):
    response = "placeholder to later display all the list of blogs"
    
    return HttpResponse(response)
# create a new method
def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, number):

    response = "placeholder to display blog ", number 
    return HttpResponse(response)

def edit(request, number):

    response = "placeholder to edit blog ", number 
    print response
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/')
