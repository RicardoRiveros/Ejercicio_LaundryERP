from django.db import models

# Create your models here.
class Empleado(models.Model):
    ROLES=[('admin', 'Administrador'), 
           ('empleado', 'Empleado')
           ]
    
    #Creando los campos de la tabla Empleados
    nombre=models.CharField(max_length=100)
    rol=models.CharField(max_length=10, choices=ROLES, default='empleado')

class Cliente(models.Model):
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    correo=models.EmailField(unique=True) #con unique=true se establece para que los correos sean unicos
    direccion=models.TextField() #Texto mas grande 

    def __str__(self):
        return self.nombre
    
