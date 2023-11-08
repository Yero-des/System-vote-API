from rest_framework import serializers
from .models import *

class ListaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lista
    fields = '__all__'