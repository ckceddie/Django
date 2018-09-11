# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from random import randint
import datetime
from .models import *


def index(request):
    context = {
        "users" : users.objects.all(),
    }
    print "=========================="
    print context
    print "=========================="

    return render(request,"users/index.html",context)


def new(request):
    return render(request, "users/new.html")

def add(request):
    users.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
    return redirect("/users")

def show(request,id):
    context = {
        "users" : users.objects.filter(id=id),
    }
    print "=========================="
    print context
    print "=========================="
    return render(request,"users/show.html",context)


def update(request):

    user = users.objects.get(id=request.POST['id'])
    user.first_name=request.POST['first_name']
    user.last_name =request.POST['last_name']
    user.email =request.POST['email']
    user.save()
    return redirect("/users")



def edit(request,id):
    print "=========================="
    print " in EDIT"
    print "=========================="
    context = {
        "users" : users.objects.filter(id=id),
    }
    print "=========================="
    print context
    print "=========================="
    return render(request,"users/edit.html",context)

def delete(request,id):
    getData=users.objects.get(id=id)
    getData.delete()
    return redirect("/users")
