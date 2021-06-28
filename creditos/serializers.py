from django.db import models
from rest_framework import serializers
from .models import usuarios,puntuacion,creditos

class creditosSerializer(serializers.ModelSerializer):
    class Meta:
        model = creditos
        fields ='__all__'
        
class puntuacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = puntuacion
        fields ='__all__'
        
        
class usuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuarios
        fields ='__all__'