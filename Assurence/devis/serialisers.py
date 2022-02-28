from rest_framework.serializers import ModelSerializer
from .models import *


class DevisMaisonSerializers(ModelSerializer):
    class Meta:
        model = Devis_Maison
        fields = '__all__'


class DevisAppartmentSerializers(ModelSerializer):
    class Meta:
        model = Devis_Maison
        fields = '__all__'


class DevisImmeubleSerializers(ModelSerializer):
    class Meta:
        model = Devis_Immeuble
        fields = '__all__'
