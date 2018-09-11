# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages

from django.shortcuts import render, HttpResponse, redirect
from random import randint
import datetime
from .models import *
# errors =[]


def index(request):
    context = {
        "users" : users.objects.all(),
    }
    return render(request,"users/index.html",context)


def new(request):
    return render(request, "users/new.html")

def add(request):
    # ================= [ Add User ]=========================
    users.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
    return redirect("/users")

def show(request,id):
    # ================= [ Show User ]=========================

    context = {
        "users" : users.objects.filter(id=id),
    }
    return render(request,"users/show.html",context)

def validation(request):
    # ================= [ Validation ]=========================

    errors =[]
    if len(request.POST['first_name']) < 1:
        errors.append("First name cannot be emply")
    if len(request.POST['email']) < 1:
        errors.append("Email  cannot be emply")
        context = {
            "users" : users.objects.filter(id=request.POST['id']),
            "err" : errors,
        }
    return errors

def update(request):
    # ================= [ Update User ]=========================

    errors=validation(request)

    if len(errors)>0:
        context = {
            "users" : users.objects.filter(id=request.POST['id']),
            "errors" : errors,
        }
        return render(request,"users/edit.html",context)
    else:
        user = users.objects.get(id=request.POST['id'])
        user.first_name=request.POST['first_name']
        user.last_name =request.POST['last_name']
        user.email =request.POST['email']
        user.save()
        return redirect("/users")



def edit(request,id):
        # ================= [ Edit User ]=========================
    context = {
        "users" : users.objects.filter(id=id),
    }
    return render(request,"users/edit.html",context)

def delete(request,id):
    # ================= [ Delete User ]========================
    getData=users.objects.get(id=id)
    getData.delete()
    return redirect("/users")
