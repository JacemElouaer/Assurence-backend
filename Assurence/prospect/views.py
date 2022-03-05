from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from  rest_framework.permissions import AllowAny
from .models import *
from .serialisers import *


# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        }
    ]
    return Response(routes)


@api_view(["POST"])
@permission_classes([AllowAny])
def save_prospect(request):
    data = request.data
    prospect = Prospect.objects.create(
        id=data["id"],
        nom=data['nom'],
        prenom=data['prenom'],
        adresse_email=data['adresse_email'],
        adress=data["adress"])
    prospect.save()
    serializer = ProspectSerializers(prospect, many=False)
    return Response(serializer.data['id'])


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_prospect(request):
    try :
        prospects = Prospect.objects.all()
    except Prospect.DoesNotExist :
        prospects = None
    serializer = ProspectSerializers(prospects, many=True)
    return Response(serializer.data)
