from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Avg, Max, Min, Sum
from django.core.paginator import Paginator , EmptyPage ,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from.forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from.models import *
from.forms import Bidform
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from.forms import LoginForm



# Create your views here.
def home(request):
    on_auction =  Product.objects.filter(on_auction=True)
    on_sale =  Product.objects.filter(on_auction=False)
    category =  Category.objects.all()
    bidders   =  Bidds.objects.all()
    product_count  =  Product.objects.filter(on_auction=True).count()
    context = {
        "bid":on_auction,
        "category":category,
        "product_count":product_count,
        "bidders":bidders,
        "on_sale":on_sale,
    
    }
    return render(request,'index.html',context)


def about(request):
    return render (request,'about.html')



def bidders(request):

    bidders = Bidder.objects.all()

    context =  {
        'bidders':bidders
    }

    return render(request,'bidders.html',context)


def faqs(request):
    return render(request,'faqs.html')


def tsandcs(request):
    return render(request, 'tsandcs.html')


def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        messages.success(request, 'Your message has been sent we will contact you as ppossible')
        
    return render(request, 'contact.html')
        


def login_process(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user=authenticate(request=request,username=username,password=password)  
            if user is not None:
                login(request=request,user=user)
                messages.success(request,f"You have successfuly logged in as {username} ")
                return redirect('home')
                
            else:
                msg = 'invalid credentials'
        else:
            msg = "error invalid creadentials"
    return render(request,'login.html',{'form':form, 'msg':msg})



def bidnow(request):
  
    return render(request,'bidnow.html')


def onsale(request):
   

    return render(request,'on_sale.html')


def product(request,id ):
    product = Product.objects.get(id=id)
    productImage = Product_img.objects.all()
    number_of_bids = Bidds.objects.filter(bid_product=product).count()
    bidds =  product.bidds_set.all().order_by('bid_time')
    highest_bid = Bidds.objects.filter(bid_product=product).aggregate(Max('bid_price'))
    lowest_bid = Bidds.objects.filter(bid_product=product).aggregate(Min('bid_price'))
    

    context = {
		'product': product,
        'number_of_bids':number_of_bids,
        'product_img':productImage ,
        'bidds':bidds,
        'highest_bid': highest_bid ,
        'lowest_bid':lowest_bid,
        
	}
    return render(request, "product_detail.html",context)


@login_required(login_url="login")
def make_bid(request,id):
    product = Product.objects.get(id=id)
    number_of_bids = Bidds.objects.filter(bid_product=product).count()
    highest_bid = Bidds.objects.filter(bid_product=product).aggregate(Max('bid_price'))
    
    g = highest_bid["bid_price__max"]
    print(g)

    form = Bidform(instance=product)

    if request.method == "POST":
        form = Bidform(request.POST,instance=product)
        if form.is_valid():
            bidder = request.user.username
            bid = form.cleaned_data['bid_price']
            b = Bidds(bid_product=product,bidder = bidder, bid_price=bid,bid_time=datetime.now())
            if number_of_bids ==  0:
                if int(bid)  < int(product.bid_start_price)+int(product.bid_gap):
                    messages.error(request, f"You bid hast to be higher than the { product.bid_start_price + product.bid_gap }.")
                    return redirect("make_bid", product.id)
                else:
                    b.save()
                    messages.success(request,f"A bid of USD { bid }.00 for  {product.id} was successfuly")
                    return redirect ('product', id=product.id)


            elif number_of_bids >= 1:
                if int(bid)  < int(g)+int(product.bid_gap):
                    messages.error(request, f"Your bid hast to be higher than the current highest bid { g + product.bid_gap }.")
                    return redirect("make_bid", product.id)

                elif int(bid)  >= int(g)+int(product.bid_gap):
                    b.save()
                    messages.success(request,f"A bid of USD { bid }.00 for  {product.id} was successfuly")
                    return redirect ('product', id=product.id)
    
        else:
            print("form is not Valid")

    else:
        form = Bidform()
    context = {
        'form':form,
        
    }
    return render (request,"add_bid.html",context)



def logout_process(request):
    logout(request)
    messages.success(request,"Logout Successfully")
    return render(request,'index.html')

