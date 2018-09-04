# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    print "===============[ index ]===================="
    request.session['amount']=0
    request.session['qty']=0
    return redirect('/amadon')

def amadon(request):
    print "===============[ amadon ]===================="
    return render(request,"Amadon/index.html")

def buy(request):
    print "===============[ buy ]===================="

    if request.POST['id']=='1' :
        price = 19.99
    elif request.POST['id']=='2' :
        price = 25
    elif request.POST['id']=='3' :
        price = 5
    elif request.POST['id']=='4' :
        price = 35
    else:
        price = 0

    qty = request.session.get('qty',0)
    total= price * int(request.POST['quantity'])
    qty = qty+int(request.POST['quantity'])

    amount = request.session.get('amount',0)
    amount=amount+total
    print "===============[ print data ]===================="
    print "request ID: "+ request.POST['id']
    print " price :" + str(price)
    print " qty :" + str(qty)
    print " total :" + str(total)
    print " amount :" + str(amount)
    print "request.session ['amount']:" +str(request.session['amount'])
    print "===============[ end print ]===================="



    request.session['amount']=amount
    request.session['total']=total
    request.session['qty']= qty
    return redirect('/checkout')

def checkout(request):
    print "===============[ checkout ]===================="
    print request.session['total']
    print "===============[ done print out total ]===================="

    total_value = request.session.get('total', 0)
    data ={
        'total': total_value
        }
    request.session['total'] =0
    return render(request,"Amadon/checkout.html",data)
