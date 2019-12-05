from django.db import models
from django.urls import reverse
import uuid



class Pasajero(models.Model):
    primer_nombre = models.CharField(max_length=100)
    primer_apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    correo_electronico = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    ##fecha_de_muerte = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['primer_apellido', 'primer_nombre','nacionalidad','correo_electronico']
        
    def get_absolute_url(self):
        return reverse('pasajero-detail', args=[str(self.id)])
        
    def __str__(self):
        return f'{self.primer_apellido}, ({self.primer_nombre})'

# Create your models here.
