from django.db import models
from datetime import datetime
from django.utils.timezone import now



# Create your models here.


class usuarios(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
    
class puntuacion(models.Model):
    puntuacion=models.CharField(max_length=30)
    
    def __str__(self):
        return self.puntuacion

class creditos(models.Model):
    deuda=models.FloatField()
    id_user=models.ForeignKey(usuarios, on_delete=models.CASCADE)
    id_puntuacion=models.ForeignKey(puntuacion, on_delete=models.CASCADE)
    AlgoritoIa=models.FloatField()
    fecha=models.DateField(default=now)
    status=models.BooleanField()
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return "%s %s" % (self.id_user,self.deuda)

