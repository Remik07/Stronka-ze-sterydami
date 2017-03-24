from django.shortcuts import get_object_or_404, render, redirect
from django import template
from django.http import Http404
from django.http import HttpResponse
from django.template import loader, RequestContext

from .models import Product, User, Address, Order
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
    counter = 0
    # get all stored Record objects
    oldProducts = Product.objects.all()

    # make dictionary of old queries
    context = {
        'appname': appname,
        'oldProducts' : oldProducts,
		'counter' : counter
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

@loggedin
def orders(request):# get all fulfilled orders
	u = request.session['username']
	user = User.objects.get(username = u)
	allOrders =  Order.objects.filter(userid = user).filter(confirmed = 1)
	address = Address.objects.get(userid = u)
	context = {
        	'appname': appname,
		'loggedin': True,
		'username' : u,
        	'allOrders' : allOrders,
		'address' : address
	}
	return render(request, 'ecommerce/orders.html', context)

@loggedin
def orderproducts(request):# get all fulfilled orders
	u = request.session['username']
	orderid = request.POST['orderid']
	products =  order.get(orderid = orderid).productid.all()

	context = {
        	'appname': appname,
		'loggedin': True,
		'username' : u,
        	'products' : products
	}
	return render(request, 'ecommerce/orderproducts.html', context)

def signup(request):
    context = { 'appname': appname }
    return render(request, 'ecommerce/signup.html', context)
	
def register(request):
	u = request.POST['username']
	e = request.POST['email']
	p = request.POST['password']
	ph = request.POST['phone']
	a1 = request.POST['address1']
	a2 = request.POST['address2']
	pc = request.POST['postcode']
	fn = request.POST['firstname']
	ln = request.POST['lastname']
	ci = request.POST['city']
	co = request.POST['country']

	user = User(username=u, email=e, password=p, phonenumber=ph, firstname=fn, lastname=ln)	
	address = Address(addressline1 = a1, addressline2 = a2, postcode = pc, city = ci, country = co, userid = user)
	user.save()
	address.save()

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
            member = User.objects.get(pk=u)
        except member.DoesNotExist:
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

@loggedin
def basket(request):
	u = request.session['username']
	user = User.objects.get(username = u)
	order = Order.objects.filter(userid = user).filter(confirmed = 0)
	if order.exists():
		allProductsInBasket = order.get().productid.all()
		return render(request, 'ecommerce/basket.html', {
			'appname': appname,
			'loggedin': True,
			'allProductsInBasket' : allProductsInBasket,
			'username' : u}
		)
	else:
		return render(request, 'ecommerce/basket.html', {
			'appname': appname,
			'loggedin': True,
			'username' : u}
		)
@loggedin
def addbasket(request):
	u = request.session['username']
	productid = request.POST['stuffNum']

	user = User.objects.get(username = u)
	order = Order.objects.filter(userid = user).filter(confirmed = 0)
	product = Product.objects.get(ProductID = productid)

	if order.exists():
		o = order.get()
	else:
		o = Order(confirmed = 0, userid = user)
		o.save()
	o.productid.add(product)


	return render(request, 'ecommerce/added.html', {
		'appname': appname,
		'loggedin': True,
		'username' : u}
	)

def removefrombasket(request):
	u = request.session['username']
	productid = request.POST['itemID']
	user = User.objects.get(username = u)
	order = Order.objects.filter(userid = user).filter(confirmed = 0)
	o = order.get()
	product = Product.objects.get(ProductID = productid)
	o.productid.remove(product)

	if order.exists():
		allProductsInBasket = order.get().productid.all()
		return render(request, 'ecommerce/basket.html', {
			'appname': appname,
			'loggedin': True,
			'allProductsInBasket' : allProductsInBasket,
			'username' : u}
		)
	else:
		return render(request, 'ecommerce/basket.html', {
			'appname': appname,
			'loggedin': True,
			'username' : u}
		)