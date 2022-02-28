from rest_framework.serializers import ModelSerializer
from .models import *


class ProspectSerializers(ModelSerializer):
    class Meta:
        model =  Prospect
        fields = '__all__'





