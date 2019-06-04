from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Fita, FamiliaComponentes, Placa

from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FamiliaComponentesViewSet(viewsets.ModelViewSet):
    queryset = FamiliaComponentes.objects.all()
    serializer_class = FamiliaComponentesSerializer      

class FitaViewSet(viewsets.ModelViewSet):
    queryset = Fita.objects.all()
    serializer_class = FitaSerializer  

class PlacaViewSet(viewsets.ModelViewSet):
    queryset = Placa.objects.all()
    serializer_class = PlacaSerializer        