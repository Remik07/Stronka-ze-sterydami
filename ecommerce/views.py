from django.shortcuts import get_object_or_404, render
from django import template
from django.http import Http404
from django.http import HttpResponse
from django.template import loader, RequestContext

from .models import Member, Product, Basket
import math

# Create your views here.

appname = 'Ecommerce Website'

def loggedin(f):
    def test(request):
        if 'username' in request.session:
            return f(request)
        else:
            return render(request, 'ecommerce/not-logged-in.html', {})
    return test

def index(request):
    # get all stored Record objects
    oldProducts = Product.objects.all()

    # make dictionary of old queries
    context = {
        'appname': appname,
        'oldProducts' : oldProducts
    }
    return render(request, 'ecommerce/index.html', context)

def shop(request):
    # get all stored Record objects
    oldProducts = Product.objects.all()
    u = request.session['username']
    context = {
        'appname': appname,
		'loggedin': True,
		'username' : u,
        'oldProducts' : oldProducts
    }
    return render(request, 'ecommerce/index.html', context)


def signup(request):
    context = { 'appname': appname }
    return render(request, 'ecommerce/signup.html', context)
	
def register(request):
    u = request.POST['username']
    e = request.POST['email']
    p = request.POST['password']
    ph = request.POST['phone']
    hn = request.POST['house']
    a1 = request.POST['address1']
    a2 = request.POST['address2']
    pc = request.POST['postcode']
    user = Member(username=u, email=e, password=p, phone=ph, house=hn, address1=a1, address2=a2, postcode=pc)
    user.save()
    context = {
        'appname': appname,
        'username' : u
    }
    return render(request, 'ecommerce/user-registered.html', context)

def login(request):
    if 'username' not in request.POST:
        context = { 'appname': appname }
        return render(request, 'ecommerce/login.html', context)
    else:
        u = request.POST['username']
        p = request.POST['password']
        try:
            member = Member.objects.get(pk=u)
        except Member.DoesNotExist:
            return HttpResponse("User does not exist")
        if p == member.password:
            request.session['username'] = u;
            request.session['password'] = p;
            return render(request, 'ecommerce/login.html', {
                'appname': appname,
                'username': u,
                'loggedin': True}
            )
        else:
            return HttpResponse("Wrong password") 

@loggedin		
def basket(request):
    u = request.session['username']
    return render(request, 'ecommerce/basket.html', {
        'appname': appname,
		'loggedin': True,
		'username' : u}
    )
	
@loggedin
def logout(request):
    if 'username' in request.session:
        u = request.session['username']
        request.session.flush()        
        context = {
            'appname': appname,
            'username': u
        }
        return render(request, 'ecommerce/logout.html', context)
    else:
        raise Http404("Can't logout, you are not logged in")