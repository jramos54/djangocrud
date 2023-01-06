from django.urls import path
from . import views

urlpatterns=[
  path('',views.home,name='home'),
  path('clientes/',views.clientes,name='clientes'),
  path('nuevocliente/',views.nuevocliente,name='nuevocliente')
]