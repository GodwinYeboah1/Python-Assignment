from __future__ import unicode_literals
from ..user_app.models import User
from django.db import models

# Create your models here.
# blue print 

class ReviewManager(models.Manager):
    def validation_check(request):
        pass

class Author(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")

class Review(models.Model):
    rating = models.IntegerField()
    review = models.TextField(max_length=1000)
    reviewer = models.ForeignKey(User, related_name="reviews")
    book = models.ForeignKey(Book, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add = True)
    objects = ReviewManager()
