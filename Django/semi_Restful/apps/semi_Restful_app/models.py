from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
# this is the class that will allow you to create new methods in the user object
    def validate(self,form_data):
        print "Validating  - {}".format(form_data)
        # validtion done here
        print " this is working models ", form_data['first_name']
        pass

        response = {
            'errors': [],
            'user': None,
            'valid': True
        }
        if len(form_data['first_name']) < 5:
            response['errors'].append('error name must be longer')
            response['valid'] = False
            print response['errors']

        else:
            print "create name here "
           


        return False

# this how we create a method in the model file 
# creating this method here allow my views file to be clean and just call out method
# self , ref to that specific instance from that class and form _data is a place holder for the request data

    def create_user(self, form_data):
# created a variable that holds the POST data
# remember to use the paramater that you gave the function
        first_name = form_data['first_name']
        last_name = form_data['last_name']
        email = form_data['email']

#  this is how you create a user in the database
# store it in a variable call user so we can refer to that variable
        user = self.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
        )
# return this variable so my views file can use it, 
# this user variable carry the create funtion
        return user


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # go look for the new methods that i found 
    # this is what this line is doing 
    objects = UserManager()

# show the type and  the data whats in it use __str__  check django shell
    def __str__(self):
        return "{} -{}".format(self.id, self.email)