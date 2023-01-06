from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import customers

# Create your views here.

def home(request):
  page=loader.get_template('home.html')
  context={}
  return HttpResponse(page.render(context,request))

def clientes(request):
  clients=customers.objects.all().values()
  tipo=type(clients)    
  page=loader.get_template('customers/viewscustomers.html')
  context={'clients':clients,'tipo':tipo}
  return HttpResponse(page.render(context,request))

def nuevocliente(request):
  page=loader.get_template('customers/newcustomer.html')
  context={}
  return HttpResponse(page.render(context,request))