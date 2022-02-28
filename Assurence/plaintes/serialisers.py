from rest_framework.serializers import ModelSerializer
from .models import *


class PlaintesSerializer(ModelSerializer):
    class Meta:
        models = Plaintes
        fields = '__all__'
