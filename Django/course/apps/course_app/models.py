from __future__ import unicode_literals

from django.db import models
class CourseManager(models.Manager):
    def validate(self, ):
        if Course['name']




# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add =True)


    