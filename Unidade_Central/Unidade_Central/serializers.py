from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Fita, FamiliaComponentes

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = '__all__'
    
class FitaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Fita
        fields = '__all__'

class FamiliaComponentesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = FamiliaComponentes
        fields = '__all__'        