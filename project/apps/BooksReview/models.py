from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class mybooks(models.Model):
    curr_user = models.ForeignKey(users, related_name="book")
    all_users = models.ManyToManyField(users, related_name="all_books")
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class review(models.Model):
    curr_user = models.ForeignKey(users, related_name="review")
    all_users = models.ManyToManyField(users, related_name="all_reviews")
    rate = models.CharField(max_length=255)
    review = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    curr_book = models.ForeignKey(mybooks, related_name="reviews")

    #
	# curr_team = models.ForeignKey(Team, related_name="curr_players")
	# all_teams = models.ManyToManyField(Team, related_name="all_players")
