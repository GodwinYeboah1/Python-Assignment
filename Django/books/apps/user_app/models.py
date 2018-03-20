from __future__ import unicode_literals

from django.db import models
from django.shortcuts import render, redirect
import re
# re name folder 
# re name your bcrypt file  and download from it from stack over flow
import bcrypt



EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# this class will be doing the heavy duty (like user validation)
# we are making our own method using the Manager class this is one way of doing it
class UserManager(models.Manager):

    def register(self,name,allias,email,password,confirm_password):
        print "this is happen in the models.py",name, allias, email, password, confirm_password   
        #  create a response dict that will allow you to store your validation errors so my views can use it
        # to send  message to the views
        response ={
            'errors': [],
            'User': None,
            'valid': True
        }

        # checking on user valid bellow if any of this is true it will involk the if statment and enter its block
        if len(name) < 1:
            response['valid'] = False
            response['errors'].append("name is required")
        
        if len(allias) < 1:
            response['valid'] = False
            response['errors'].append("allias is  required")

        # email validtion takes three part check the length, 
        # check if the email is in the write format
        # check if the email is in our database
        
        if len(email) < 1:
            response['valid'] = False
            response['errors'].append("email is required")
        elif not EMAIL_REGEX.match(email):
            response['valid'] = False
            response['errors'].append("invailed email")
        else:
            # this filter() method return a list of emails if matched in our database
            # we used a list_of_email varible to hold the return list of emails
            # remeber to change the email = email.lower() because we lower method when we save the data it in the 
            list_of_email = User.objects.filter(email= email.lower())
            if len(list_of_email) > 0:
                response['valid'] = False
                response['errors'].append("email already exist")

        if len(password) < 8:
            response['valid'] = False
            response['errors'].append("password has to be 8 character long")

        if  confirm_password != password:
            response['valid'] = False
            response['errors'].append("password does not match")

        # validtion for true comes bellow  if it did not triggr my if statement condition
        # this is where you want to create your user 
        if response['valid'] :
            response['user'] = User.objects.create(
                name= name,
                allias =allias,
                # incase user use a cap case with the same email we will still save it in our database
                email = email.lower(),
                # we encrpyt our database 
                password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()),
            )
        # this is what you want to return so you can see your result
        return response


    def login(self, email, password):
         #  create a response dict that will allow you to store your validation errors so my views can use it
        # to send  message to the views
        response ={
            'errors': [],
            'User': None,
            'valid': True
        }

        if len(email) < 1:
            response['valid'] = False
            response['errors'].append("email is required")
        elif not EMAIL_REGEX.match(email):
            response['valid'] = False
            response['errors'].append("invailed email")
        else:
            # this filter() method return a list of emails if matched in our database
            # we used a list_of_email varible to hold the return list of emails
            # remeber to change the email = email.lower() because we lower method when we save the data it in the 
            list_of_email = User.objects.filter(email= email.lower())

            # this is when you already in database 
            if len(list_of_email) == 0:
                response['valid'] = False
                response['errors'].append("email does not exist")      
            
        if len(password) < 8:
            response['valid'] = False
            response['errors'].append("password has to be 8 character long")

        # if  confirm_password != password:
        #     response['valid'] = False
        #     response['errors'].append("password does not match")

        # validtion for true comes bellow  if it did not triggr my if statement condition
      
        if response['valid'] :
            if bcrypt.checkpw(password.encode(), list_of_email[0].password.encode()):
                response['user'] = list_of_email[0]
                return response
            else:
                response['valid'] = False
                response['errors'].append("incorrect password")
                return redirect('/')

        return response


# Create your models here.
# this is the user class that respenset a database table that django will create for us
class User(models.Model):
    # this bellow represent a colum 
    #  model.charField store informtion that comes in the database as string 
    # model.datetimeField store event times
    name = models.CharField(max_length = 255)
    allias = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now =True)
    # the reason why i want to make a migrations is because it looks any changes that need to be done to create the database
    # this is the reason we start with 13 unapplied migration

    # this is when we create a object after creating a Manager class we do this in here because all User clas will be inheriant
    # there attribute from here
    objects = UserManager()
