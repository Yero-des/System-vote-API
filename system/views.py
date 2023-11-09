from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework import viewsets
from .models import *
from .serializers import *

# API
class ListaViewSet(viewsets.ModelViewSet):
  queryset = Lista.objects.all()
  serializer_class = ListaSerializer

def votacion(request):

  lista = Lista.objects.all()
  cantidad = lista.count()

  context = {
    "lista": lista,
    "cantidad": cantidad,
  }

  return render(request, 'cantidatos.html', context)

def voto_confirmado(request):
  return render(request, 'confirmar.html')
  
def aumentar_votos(request, lista_id):

  if request.method == 'POST':

    lista = Lista.objects.get(id=lista_id)
    lista.votos += 1
    lista.save()

    url = reverse('voto_confirmado')

    return redirect(url)

