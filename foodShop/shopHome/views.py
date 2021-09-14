from django.shortcuts import render, get_object_or_404,redirect
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,InvalidPage,EmptyPage

# Create your views here.
def home(request,c_slug=None):
    c_page=None
    prod=None
    if c_slug!=None:
        c_page=get_object_or_404(category,slug=c_slug)
        prod=product.objects.filter(categ=c_page,available=True)
    else:
        prod=product.objects.all().filter(available=True)
    cat=category.objects.all()
    paginator=Paginator(prod,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pr=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pr=Paginator.page(paginator.num_pages)

    return render(request,'index.html',{'pro': prod,'ct':cat,'pg':pr})

def productdetail(request,c_slug,product_slug):
    try:
        prod=product.objects.get(categ__slug=c_slug,slug=product_slug)
    except Exception  as e:
        raise e
    return render(request,'item.html',{'pro':prod})

def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=product.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    else:
        redirect('/')

    return render(request,'search.html',{'qr':query,'pro':prod})