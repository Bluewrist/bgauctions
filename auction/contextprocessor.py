from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Avg, Max, Min, Sum
from django.core.paginator import Paginator , EmptyPage ,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from.forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from.models import Bidds,Product,Contact,Bidder,Product_img,Category,Auction_details
from.forms import Bidform
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from.forms import LoginForm






def bidnow(request):
    q =  request.GET.get('q') 
    if q == None:
        on_auction  = Product.objects.filter(on_auction=True)
    else:
        on_auction = Product.objects.filter(Q(category__name__icontains=q)|
                                Q(product_name__icontains=q)|
                                Q(product_description__icontains=q)
                                )

    category =  Category.objects.all()
    bidders   =  Bidds.objects.all()
    product_count  =  on_auction.count()
    page = request.GET.get('page')
    paginator = Paginator(on_auction, 20)
    try:
        on_auction = paginator.page(page)        
    except PageNotAnInteger:
        on_auction = paginator.page(1)
    except EmptyPage:
        on_auction = paginator.page(paginator.num_pages)
    context = {
        "product":on_auction,
        "category":category,
        "product_count":product_count,
        "bidders":bidders,
        
    }
    return context



def onsale(request):
    q =  request.GET.get('q') 
    if q == None:
        on_auction  = Product.objects.filter(on_auction=False)
    else:
        on_auction = Product.objects.filter(Q(category__name__icontains=q)|
                                Q(product_name__icontains=q)|
                                Q(product_description__icontains=q)
                                )
    category =  Category.objects.all()
    bidders   =  Bidds.objects.all()
    product_count  =  on_auction.count()
    page = request.GET.get('page')
    paginator = Paginator(on_auction, 20)
    try:
        on_auction = paginator.page(page)        
    except PageNotAnInteger:
        on_auction = paginator.page(1)
    except EmptyPage:
        on_auction = paginator.page(paginator.num_pages)
    context = {
        "product":on_auction,
        "category":category,
        "product_count":product_count,
        "bidders":bidders,
    }
    return context
