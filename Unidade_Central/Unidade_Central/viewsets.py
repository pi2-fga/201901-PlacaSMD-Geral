from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Fita, FamiliaComponentes

from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class FitaViewSet(viewsets.ModelViewSet):
    queryset = Fita.objects.all()
    serializer_class = FitaSerializer

class FamiliaComponentesViewSet(viewsets.ModelViewSet):
    queryset = FamiliaComponentes.objects.all()
    serializer_class = FamiliaComponentesSerializer    