from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serialisers import *
from .models import *
# Create your views here.



@api_view(["GET"])
def get_all_plaintes(request):
    try:
        plaintes =  Plaintes.objects.all()
    except Plaintes.DoesNotExist :
        plaintes = None

    serializers = PlaintesSerializer(plaintes ,  many=True)
    return Response(serializers.data)


@api_view(["POST"])
def save_plainte(request):
    data = request.data
    prospect = Plaintes.objects.create(
        email=data['emain'],
        answer=data['answer'],
        sujet=data["sujet"])
    prospect.save()
    serializer = PlaintesSerializer(prospect, many=False)
    return Response(serializer.data['id'])




