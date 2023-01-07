from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import customers
from .forms import nuevoclienteform

# Create your views here.

def home(request):
  page=loader.get_template('home.html')
  context={}
  return HttpResponse(page.render(context,request))

def clientes(request):
  clients=customers.objects.all().values()   
  page=loader.get_template('customers/viewscustomers.html')
  context={'clients':clients}
  return HttpResponse(page.render(context,request))

def nuevocliente(request):
  page=loader.get_template('customers/newcustomer.html')
  form=nuevoclienteform
  cliente_existente='El cliente ya existe'
  if request.method == 'POST':
    form=nuevoclienteform(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/clientes')
    else:
      return redirect('/clientes',cliente_existente)
  context={'form':form}
  
  return HttpResponse(page.render(context,request))