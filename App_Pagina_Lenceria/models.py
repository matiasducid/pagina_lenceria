#from tkinter import CASCADE
# Create your models here.
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Productor(models.Model):
    identificador = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=100)

class Producto(models.Model):
    identificador = models.IntegerField(primary_key=True)
    precio_compra = models.FloatField(default=0)
    precio_venta = models.FloatField(default=0)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    talle = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    dni = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    def __str__(self):
        return self.nombre

class Factura(models.Model):
    identificador = models.IntegerField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    #[TODO] agregar la lista de productos comprados.
    fecha = models.DateField(auto_now=True)
    hora = models.TimeField(auto_now=True)
    def __str__(self):
        return self.cliente
