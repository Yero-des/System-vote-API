from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# API
class ListaViewSet(viewsets.ModelViewSet):
  queryset = Lista.objects.all()
  serializer_class = ListaSerializer

def votacion(request):
  context = {
    "cantidatos": Lista.objects.all(),
  }

  return render(request, 'cantidatos.html', context)
