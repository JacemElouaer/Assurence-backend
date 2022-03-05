from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serialisers import *
from .models import *
from prospect.models import Prospect
from prospect.serialisers import *
import time


# Create your views here.


@api_view(["GET"])
@permission_classes([AllowAny])
def get_devis_maison(request):
    try:
        Devis_Maisons = Devis_Maison.objects.all()
    except Devis_Maison.DoesNotExist:
        Devis_Maisons = None
    serializer = DevisMaisonSerializers(Devis_Maisons, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([AllowAny])
def save_devis_maison(request):

    data = request.data
    id = data['id']
    time.sleep(1)
    print("this is id :  ", id)
    try:
        prospect = Prospect.objects.get(id=id)
    except Prospect.DoesNotExist:
        prospect = "i can't find it"

    print(prospect)

    devis_maison = Devis_Maison.objects.create(
        prospect=prospect,
        adresse=data['adresse'],
        complement=data['complement'],
        email_prospect=data['email_prospect'],
        besoin_resiliation=data['besoin_resiliation'],
        type_residence=data['type_residence'],
        Vérnada=data["Veranda"],
        Cheminée=data["Cheminée"],
        Piscine=data["Piscine"],
        type_propriete=data['type_propriete'],
        interraction=data['interraction'],
        Surface=data['Surface'],
        nbrChambre=data['nbrChambre'],
        dependance=data['dependance'],
        surface_depandance=["surface_depandance"],
        periode_construction=['periode_construction'],
        type_resiliation=data['type_resiliation'],
        nbr_sinistre=data['nbr_sinistre'],
        resiliation=data['resiliation'],
        periode_resiliation=data['periode_resiliation'],
        date_resiliation=data['date_resiliation'],
        Tarification=data['Tarification'],
        franchise=data['franchise'])
    serializer = DevisMaisonSerializers(devis_maison)
    print(serializer.data)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_devis_apartement(request):
    try:
        Devis_Maisons = Devis_Maison.objects.all()
    except Devis_Maison.DoesNotExist:
        Devis_Maisons = None
    serializer = DevisMaisonSerializers(Devis_Maisons, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([AllowAny])
def save_devis_apartment(request):
    data = request.data
    try:
        prospect = Prospect.objects.get(id=data['id'])
    except Prospect.DoesNotExist:
        prospect = "i can't find it"

    print(prospect)
    devis_apartment = Devis_Maison.objects.create(
        prospect=prospect,
        adresse=data['adresse'],
        complement=data['complement'],
        email_prospect=data['email_prospect'],
        besoin_resiliation=data['besoin_resiliation'],
        type_residence=data['type_residence'],
        type_propriete=data['type_propriete'],
        interraction=data['interraction'],
        Surface=data['Surface'],
        nbrChambre=data['nbrChambre'],
        dependance=data['dependance'],
        surface_depandance=data["surface_depandance"],
        type_resiliation=data['type_resiliation'],
        nbr_sinistre=data['nbr_sinistre'],
        resiliation=data['resiliation'],
        periode_resiliation=data['periode_resiliation'],
        date_resiliation=data['date_resiliation'],
        Tarification=data['Tarification'],
        franchise=data['franchise'])
    serializer = DevisAppartmentSerializers(devis_apartment, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_devis_immeuble(request):
    try:
        devis_Immeuble = Devis_Immeuble.objects.all()
    except Devis_Immeuble.DoesNotExist:
        devis_Immeuble = None
    serializer = DevisMaisonSerializers(devis_Immeuble, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([AllowAny])
def save_devis_immeuble(request):
    data = request.data
    try:
        prospect = Prospect.objects.get(id=data['id'])
    except Prospect.DoesNotExist:
        prospect = "i can't find it"

    print("this is " , prospect)
    devis_immeuble = Devis_Immeuble.objects.create(
        prospect=prospect,
        adresse=data['adresse'],
        complement=data['complement'],
        surface_immeuble=data['surface_immeuble'],
        nombre_lots=data['nombre_lots'],
        Niveau_immeuble=data['Niveau_immeuble'],
        Niveau_sous_sol=data['Niveau_sous_sol'],
        Parking=data['Parking'],
        type_propriete=data['type_propriete'],
        type_copropriete=data['type_copropriete'],
        type_batiment=data['type_batiment'],
        periode_construction=data['periode_construction'],
        installation=data['installation'],
        traveaux=data['traveaux'],
        usage_immeuble=data['usage_immeuble'],
        activite_commerciale=data['activite_commerciale'],
        occupation=data['occupation'],
        taux_proprietaire=data['taux_proprietaire'],
        nbr_sinistre=data['nbr_sinistre'],
        type_entreprise=data['type_entreprise'],
        date_assemblee=data['date_assemblee'],
        ancien_assurence=data['ancien_assurence'],
        resiliation=data['resiliation'],
        Tarification=data['Tarification'],
        franchise=data['franchise'],
        email_prospect=data['email_prospect'])
    serializer = DevisAppartmentSerializers(devis_immeuble, many=False)
    return Response(serializer.data)
