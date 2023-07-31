from rest_framework import serializers
from djangoAssignment import models

class placesSerializer(serializers.ModelSerializer):
     
     class Meta:
         model = models.Place
         fields = ['name','description']
     