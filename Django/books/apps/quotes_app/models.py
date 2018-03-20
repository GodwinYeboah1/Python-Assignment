from __future__ import unicode_literals

from django.db import models




# Create your models here.
class Quote_by(models.Model):
    quote_by = models.CharField(max_length = 255)
    messages = models.TextField(max_length = 1000)
    