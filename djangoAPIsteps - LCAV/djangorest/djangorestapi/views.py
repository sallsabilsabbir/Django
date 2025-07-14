from django.shortcuts import render
from . models import Aiquest
from . serializers import AiquestSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.

# for get and post

class AiquestList_Creat(ListCreateAPIView):

    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer

# for retrive, put and delete
    
class AiquestRetrieve_Update_Destroy(RetrieveUpdateDestroyAPIView):

    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer
    
    
    