from django.shortcuts import render
from rest_framework.response import Response
from app.models import *
from app.serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated




# Create your views here.


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def SchoolJsonData(request):
    SOD=School.objects.all()
    JOD=SchoolModelSerializers(SOD,many=True)
    jsondata=JOD.data
    return Response(jsondata)