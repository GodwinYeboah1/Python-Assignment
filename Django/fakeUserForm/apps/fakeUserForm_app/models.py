from __future__ import unicode_literals 

from django.db import models 

#  when i want to use regural expersion/ regex  
# this meams that i want my email or whatever to match a certain pattern
import re
import bcrypt
# this is how you create a regural expersion  email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


#  need to encrypt my password with bcrypt inorder to proctect it 
# import bcrypt

# Create your models here.

class UserManager(models.Manager):
    def login(self, email, password):
        
        response ={
            "errors": [],
            "user" : None,
            "valid": True
        }

        # want to check to the email
        if len(email) < 1:
            response["errors"].append('email is required')
                # print response['errors']
            response["valid"] = False
            
            # # case when they dont have a correct email this condition will be activate
        elif not EMAIL_REGEX.match(email):
            response["errors"].append('invild email')
            print response['errors']
            response["valid"] = False
                   
        list_of_emails = User.objects.filter(email=email)
        

        # check to see if the email is in the database 
        if len(list_of_emails) == 0:
            response["errors"].append('Email doesnt exists')
                    # print response['errors']
            response["valid"] = False
        # if list_of_emails[0].password == bcrypt.hashpw(password.encode():
        #     print "login in succesfully"

            # # we want our user to have 8 length
        if len(password) < 8:
            response["errors"].append('password must be 8 characters or more ')
            # print response['password']
            response["valid"] = False

        # check password
    def register(self, name, allias,email, password, confirm_password):
        print "inside the model", name, allias, email , password, confirm_password
        #  uses dict to store error message and i will be ale to use it in my views pages
        response = {
            #  made  error assign to a empty array keyword so we can use it to append my error message and display on the views, page
            "errors": [" "],
            #  user
            "user": None,

            "valid": True
            }
        
        # to validate user input, we will do it here so we can use it in the views
        # we do this by using the function len( name of the paramaters that you want to check ) 

        #  validating name 
        # only if the input field for name is invalid will this message show 

        if len(name) < 2:
        # response['errors'].append('name is required')
            response["errors"].append('name is required')
            # print response['errors']
            response["valid"] = False
        
            # #  validating alias 
            # # only if the input field for alis is invalid will this message show 
        if len(allias) < 2:
            response["errors"].append('allias is required')
                # print response['allias']
            response["valid"] = False
                
            # #  validating email 
            # # only if the input field for email is invalid will this message show 
        if len(email) < 1:
            response["errors"].append('email is required')
                # print response['errors']
            response["valid"] = False
            
            # # case when they dont have a correct email this condition will be activate
        elif not EMAIL_REGEX.match(email):
            response["errors"].append('invild email')
                
                # check this one later
            print response['errors']
            response["valid"] = False
        # else:
            # # if the email exist in our database then we want to make sure user do not use the same email thats in our database
            # # create a variable that will store emails in our database
            
        list_of_emails = User.objects.filter(email=email)
                #  if we have an two match name this condition is involk 
        if len(list_of_emails) == 0:
            response["errors"].append('Email already exists')
                    # print response['errors']
            response["valid"] = False

            # # we want our user to have 8 length
        if len(password) < 8:
            response["errors"].append('password must be 8 characters or more ')
            # print response['password']
            response["valid"] = False

        # #  we also want to make sure that the confirm password is equal to the orginal password they enter
        # # if not, we want to validate the user and tell them that the password does not match 
        if confirm_password != password:
            response["errors"].append('Password must match confirm password')
            # print response["errors"]
            response["valid"] = False

        if response["valid"]:
            #  make sure dont forget the comma,
            response["user"] = User.objects.create(
            name = name,
            allias = allias,
            # so if anyone enters lowers case email it will validate through because it will be lowercase
            email = email.lower(),
            # DO NOT STORE PASSWORD AS REGURAL PLAIN TEXT YOU NEED TO IMPORT bcrypt
            password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            )

            # print response["user"]
            # print response['errors']

            return response
        return False

class User(models.Model):
    #  tables in the database
    name = models.CharField(max_length=255)
    allias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now = True)
    # .....  need this inorder to create a object  make sure its in side the blueprint 
    # pretty much allows us to use the method that we created ourself
    objects = UserManager()

