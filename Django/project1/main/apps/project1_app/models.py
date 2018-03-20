from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from datetime import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def login(self, email, password):
        
        response={
            "errors":[],
            "user":None,
            "valid":True
        }

        if len(email) < 1:
            response["valid"] = False
            response["errors"].append("Email is required")
        
        elif not EMAIL_REGEX.match(email):
            response["valid"] = False
            response["errors"].append("Invalid Email")
        else:
            list_of_emails = User.objects.filter(email=email.lower())
            if len(list_of_emails) == 0:
                response["valid"] = False
                response["errors"].append("Email does not exist")
        if len(password) < 8:
            response["valid"] = False
            response["errors"].append("Password must be 8 characters or more")
        
        if response["valid"]:
            if bcrypt.checkpw(password.encode(), list_of_emails[0].password.encode()):
                response["user"] = list_of_emails[0]
            else:
                response["valid"] = False
                response["errors"].append("Incorrect Password")
        return response
    
    def register(self, name, alias, email, password, confirm_password, bday):
        now=datetime.now()
    
        response={
            "errors":[],
            "user": None,
            "valid": True
        }
        if len(name) < 1:
            response["valid"] = False
            response["errors"].append("Name is required")

        if len(alias) <1:
            response["valid"] = False
            response["errors"].append("Alias is required")

        if len(email) < 1:
            response["valid"] = False
            response["errors"].append("Email is required")
        
        elif not EMAIL_REGEX.match(email):
            response["valid"] = False
            response["errors"].append("Invalid Email")
        else:
            list_of_emails=User.objects.filter(email=email)
            if len(list_of_emails) > 0:
                response["valid"] = False
                response["errors"].append("Email already exists")
        if len(password) < 8:
            response["valid"] = False
            response["errors"].append("Password must be 8 characters or more")
        
        if confirm_password != password:
            response["valid"] = False
            response["errors"].append("Password must match Confirm Password")
        if len(bday) < 1:
            response["valid"]=False
            response["errors"].append('Bday is required!')
        elif now < datetime.strptime(bday,'%Y-%m-%d'):
            response["valid"]=False
            response["errors"].append('Bday cant be in the future!')

        if response["valid"]:
            response["user"] = User.objects.create(
                name=name,
                alias=alias,
                email=email.lower(),
                password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()),
                bday=bday,
            )
        return response

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    bday = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    objects = UserManager()

class Quote(models.Model):
    posted_by = models.ForeignKey(User, related_name= "user_posts")
    author = models.CharField(max_length=45)
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    favoring_users=models.ManyToManyField(User, related_name="fav_quotes")#taking users from users, this is a list from the user table
class Favorite(models.Model):
    user = models.ForeignKey(User, related_name= "user_favorites")
    quote = models.ForeignKey(Quote, related_name = "quote_favorites")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
