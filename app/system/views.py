from rest_framework import viewsets
from .models import *
from .serializers import *


class ListaViewSet(viewsets.ModelViewSet):
  queryset = Lista.objects.all()
  serializer_class = ListaSerializer
