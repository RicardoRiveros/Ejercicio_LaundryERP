from django.db import models
from usuarios.models import Cliente, Empleado

# Create your models here.
class Prenda(models.Model):
    tipo_prenda=models.CharField(max_length=50)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    descripcion=models.TextField()

    def __str__(self):
        return self.tipo_prenda
    
#Creacion de modelo de Orden de servicio 
class OrdenesDeServicio(models.Model):
    ESTADOS=[
        ('pendiente', 'Pendiente'),
        ('proceso', 'En Proceso'),
        ('completada', 'Completada')
    ]

    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado=models.ForeignKey(Empleado, on_delete=models.SET_NULL,null=True)
    prendas=models.ManyToManyField(Prenda) #Se asocia mas de una prenda a la orden y la misma prenda puede estar en varias ordenes
    fecha_creacion=models.DateField(auto_now_add=True)
    estado=models.CharField(max_length=20 , choices=ESTADOS, default='pendiente') #'pendiente', va el valor no la etiqueta
    total=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pago_realizado=models.BooleanField(default=False)

    #Calculo del total de la orden sumando los precios de las prendas asociadas
    def calculo_total(self):
        self.total=sum(prenda.precio for prenda in self.prendas.all())
        self.save()


    def __str__(self):
        return f"Orden #{self.id} - {self.cliente.nombre} - {self.estado} - {self.total}"