from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# this class will be doing the heavy duty (like user validation)
# we are making our own method using the Manager class this is one way of doing it

class registrationManager(models.Manager):

    def register(self,userName,alias,email,password,confirm_password):
        print "this is happen in the models.py",userName, alias, email, password, confirm_password   
        #  create a response dict that will allow you to store your validation errors so my views can use it
        # to send  message to the views
        response ={
            'errors': [],
            'User': None,
            'valid': True
        }

        # checking on user valid bellow if any of this is true it will involk the if statment and enter its block
        if len(userName) < 1:
            response['valid'] = False
            response['errors'].append("name is required")
        
        if len(alias) < 1:
            response['valid'] = False
            response['errors'].append("alias is  required")

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
            list_of_emails = registration.objects.filter(email= email.lower())
            if len(list_of_emails) > 0:
                response['valid'] = False
                response['errors'].append("email already exist")

        if len(password) < 8:
            response['valid'] = False
            response['errors'].append("Password has to be 8 character long")

        if  confirm_password != password:
            response['valid'] = False
            response['errors'].append("Password does not match")

        # validtion for true comes bellow  if it did not triggr my if statement condition
        # this is where you want to create your user 
        if response['valid'] :
            response['user'] = registration.objects.create(
                userName= userName,
                alias =alias,
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
            list_of_emails = registration.objects.filter(email= email.lower())

            # this is when you already in database 
            if len(list_of_emails) == 0:
                response['valid'] = False
                response['errors'].append("email does not exist")      
            
        if len(password) < 8:
            response['valid'] = False
            response['errors'].append("password has to be 8 character long")

        if response['valid'] :
            if bcrypt.checkpw(password.encode(), list_of_emails[0].password.encode()):
                response['user'] = list_of_emails[0]
                return response
            else:
                response['valid'] = False
                response['errors'].append("incorrect password")
                return redirect('quotes/')
        return response


class contributeQuotes_manager(models.Manager):
    def contributeQuotes_validation(self, quotedBy, quotesBy_messages):
        print "this is in my contributesQuotes ", quotedBy, quotesBy_messages

# class quotesManager(models.Manager):
#     def quotesValidate(models.Manager):

        
# Create your models here.
class registration(models.Model):
    userName = models.CharField(max_length =255)
    alias = models.CharField(max_length =255)
    password = models.CharField(max_length =255)
    email = models.CharField(max_length =255)
    # date_of_birth = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = registrationManager()
    
class favorites(models.Model):
    postedBy = models.CharField(max_length=255)
    messages = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
class quotes(models.Model):
    postedBy = models.CharField(max_length=255)
    messages = models.TextField()
    favorites = models.ForeignKey(favorites related_name=quotes)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class contributeQuotes(models.Model):
    quotedBy = models.CharField(max_length=255)
    quotesBy_messages = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
