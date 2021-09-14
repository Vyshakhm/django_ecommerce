from django.shortcuts import render,redirect,get_object_or_404
from shopHome.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def cart_details(request,tot=0,count=0,ct_item=None):
    try:
        ct=cartlist.objects.get(cartid=c_id(request))
        ct_item=item.objects.filter(cart=ct)
        for i in ct_item:
            tot += (i.prod.price * i.quantity)
            count += i.quantity
    except ObjectDoesNotExist:
        pass

    return render(request,'cart.html',{'ci':ct_item,'tot':tot,'count':count})


def c_id(request):
    ct_id=request.session.session_key
    if not  ct_id:
        ct_id=request.session.create()
    return ct_id

def add_cart(request,product_id):
    prodt=product.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cartid=c_id(request))
        ct.save()
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cartid=c_id(request))
        ct.save()
    try:
        c_item=item.objects.get(prod=prodt,cart=ct)
        if c_item.quantity < c_item.prod.stock:
            c_item.quantity+=1
        c_item.save()
    except item.DoesNotExist:
        c_item=item.objects.create(prod=prodt,quantity=1,cart=ct)
        c_item.save()
    return redirect('cartdetails')


def min_cart(request,product_id):
    ct=cartlist.objects.get(cartid=c_id(request))
    prodt=get_object_or_404(product,id=product_id)
    ct_item=item.objects.get(prod=prodt,cart=ct)
    if ct_item.quantity > 1:
        ct_item.quantity -= 1
        ct_item.save()
    else:
        ct_item.delete()
    return  redirect('cartdetails')

def cart_delete(request,product_id):
    ct=cartlist.objects.get(cartid=c_id(request))
    prodt=get_object_or_404(product,id=product_id)
    ct_item=item.objects.get(prod=prodt,cart=ct)
    ct_item.delete()
    return redirect('cartdetails')

def checkout(request):

    return render(request,'payment.html')