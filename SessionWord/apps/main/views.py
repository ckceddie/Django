# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
import datetime
# Create your views here.
def index(request):
    print "========================[ index ]==============================="
    request.session['inputWord']=[]
    print request.session['inputWord']

    return redirect('/session_words')

def session_words(request):
    return render(request,"SessionWord/index.html")




def add_word(request):
    print "========================[ add_word ]==============================="
    temp=[]
    now = datetime.datetime.now()
    # get data from session -----
    for a in request.session['inputWord']:
        temp.append(a)
    # get data from request form -------
    bigFont = request.POST.get('bigFont', 0)

    get_value = {
            'inputWord': request.POST['inputWord'],
            'color':request.POST['color'],
            'bigFont':bigFont,
            'dateTime':str(now)
        }

    temp.append(get_value)
    request.session['inputWord']=temp
    return redirect('/session_words')


def clear(request):
    print "========================[ clear ]==============================="

    request.session.clear()
    return redirect('/')
