from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'listas', ListaViewSet)

urlpatterns = [
  path('', votacion, name="votacion"),
  path('voto_confirmado/', voto_confirmado, name="voto_confirmado"),
  path('aumentar_votos/<int:lista_id>/', aumentar_votos, name='aumentar_voto'),
  path('api/', include(router.urls)),
]