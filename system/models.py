from django.db import models

class Lista(models.Model):

  id = models.AutoField(primary_key=True)  
  nombre = models.CharField(max_length=250, unique=True)
  descripcion = models.CharField(max_length=250)
  alcalde = models.CharField(max_length=250)
  imagen = models.ImageField(upload_to='img', null=True)
  simbolo = models.ImageField(upload_to='symbol', null=True)
  votos = models.IntegerField(default=0)

  def __str__(self):
    return f"{self.nombre} => Votos: {self.votos}"
