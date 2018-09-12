# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from random import randint
import datetime
from .models import *
# errors =[]


def index(request):

    context = {
        # "users" : users.objects.all(),
    }
    return render(request,"register/index.html",context)

def success(request):
    context = {
        "users" : users.objects.all(),
    }
    return render(request,"register/index.html",context)

def register(request):
    error=validation(request)
    if len(error)>0:
        context = {
            "errors" : error
        }
        return render(request,"register/index.html",context)
    else:
        try:
            findData= users.objects.get(email=request.POST['email'],password=request.POST['password'])
        except:
            findData = ""

        if not findData == "" :
            err=[]
            err.append("Register failed")
            err.append("Email is already existed! Please try register again")

            context = {
                "errors" : err
            }
            return render(request,"register/index.html",context)
        else:
            users.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=request.POST['password'])
            findData= users.objects.get(email=request.POST['email'],password=request.POST['password'])
            request.session['id'] = findData.id
            context = {
                "message" : "Successfully registered",
                "first_name"  : findData.first_name,
                "last_name":findData.last_name
                }
            return render(request,"register/success.html",context)


def login(request):
    try:
        findData= users.objects.get(email=request.POST['email'],password=request.POST['password'])
    except:
        findData = ""

    if findData == "" :
        err=[]
        err.append("Login failed")
        context = {
            "errors" : err
        }
        return render(request,"register/index.html",context)
    else:
        request.session['id'] = findData.id
        context = {
                "message" : "Successfully registered",
                "first_name"  : findData.first_name,
                "last_name":findData.last_name
            }
        return render(request,"register/success.html",context)

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def validation(request):
    # ================= [ Validation ]=========================
    errors =[]
    if len(request.POST['first_name']) < 2:
        errors.append("First name cannot be less than 2 characters;")

    if not request.POST['first_name'].isalpha():
        errors.append("First Name - Error : letters only")

    if hasNumbers(request.POST['first_name']):
        errors.append("First Name - Error : letters only ( Number should not included)")

    if not request.POST['last_name'].isalpha():
        errors.append("Last Name - Error : letters only")
    if hasNumbers(request.POST['first_name']):
        errors.append("First Name - Error : letters only ( Number should not included)")

    if len(request.POST['last_name']) < 2:
        errors.append("Last name cannot be less than 2 characters;")

    if len(request.POST['email']) < 1:
        errors.append("Email cannot be emply")

    if not '@' in request.POST['email']:
        errors.append("Email format invalid")

    if len(request.POST['password']) > 8:
        errors.append("Password incorrect : No fewer than 8 characters in length ")

    if not request.POST['password'] == request.POST['re-password']:
        errors.append("Password Confirmation doesn't match ")

    return errors
