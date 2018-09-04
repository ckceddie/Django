# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Inside views.py
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    print "===============[ index ]===================="
    request.session['times'] = 0
    return render(request,"survey/index.html")

def back(request):
    print "===============[ back ]===================="
    return render(request,"survey/index.html")

def process(request):
    print "===============[ process ]===================="
    request.session['times'] += 1
    request.session['myName']=request.POST['myName']
    request.session['location']=request.POST['location']
    request.session['language']=request.POST['language']
    request.session['comment']=request.POST['comment']
    return redirect("/result")

def result(request):
    return render(request,"survey/result.html")
