from django.shortcuts import render
from . models import Aiquest
from . serializers import AiquestSerializer
from rest_framework import viewsets


# Create your views here.

# for List, create, retrive, put and delete
    
class AiquestModel_View_Set(viewsets.ModelViewSet):

    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer
    
    
    