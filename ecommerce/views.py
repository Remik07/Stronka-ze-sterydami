from django import template
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Member, Records
import math

# Create your views here.

appname = 'Ecommerce Website'

def index(request):
    context = {
        'appname': appname,
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