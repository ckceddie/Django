from __future__ import unicode_literals

from django.db import models

# Create your models here.

class userManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 5:
            errors["first_name"] = "First name should be more than 5 characters"
        if len(postData['email']) < 10:
            errors["email"] = "Email should be more than 10 characters"
        return errors


class users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
   # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = userManager()
    # *************************
