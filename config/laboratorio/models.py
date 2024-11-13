from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from datetime import date
# Create your models here.

# Modelo Laboratorio
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100,default='')
    pais = models.CharField(max_length=100,default='')
    
    def __str__(self):
        return self.nombre


# Modelo DirectorGeneral
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio =  models.OneToOneField(Laboratorio,on_delete=models.CASCADE,related_name='director_general') 
    especialidad = models.CharField(max_length=100,default='')
    
    def __str__(self):
        return self.nombre


# Modelo Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='productos')
    f_fabricacion = models.IntegerField(validators=[MinValueValidator(2015)],help_text="Ingrese solo el año de fabricación")
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)
    
    

    def __str__(self):
        return self.nombre


