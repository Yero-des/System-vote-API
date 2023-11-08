from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'listas', ListaViewSet)

urlpatterns = [
  path('', votacion, name="votacion"),
  path('api/', include(router.urls)),
]