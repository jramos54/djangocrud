from django.db import models

# Create your models here.

class customers(models.Model):
  id_customer=models.BigAutoField(primary_key=True)
  nombre_cliente=models.TextField(max_length=50)
  apellido_cliente=models.TextField(max_length=50)

  def __str__(self):
    return self.id_customer + ' - ' + self.nombre_cliente + ' ' + self.apellido_cliente
  
