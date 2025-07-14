from django.shortcuts import render
from . models import Aiquest
from . serializers import AiquestSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])

def aiquest_create (request, pk= None):

    #-------------------    GET     -----------------------

    if request.method == 'GET':
        id = pk
    #  for specif id
        if id is not None:
            try:
                ai = Aiquest.objects.get(id=id)
                serializer = AiquestSerializer(ai)
                return Response(serializer.data)
            except Aiquest.DoesNotExist:
                # return Response({"msg": " Not found"}, status=status.HTTP_404_NOT_FOUND)    or
                return Response([], status=status.HTTP_200_OK)
        
    # for all data 
        # import and store complex data into one variable from model:
        ai = Aiquest.objects.all()

        # convert/serialize into python dict:(import and use from serializers.py)
        # many= True : used because of more than one object inside AiquestSerializer
        serializer = AiquestSerializer(ai, many=True)

        # convert python dict to JSON and return :
        return Response(serializer.data)
    

    #-------------------    POST     -----------------------
    
    if request.method == 'POST':
        serializer = AiquestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Successfully Insert Data"})
        return Response(serializer.errors)
    

    #-------------------     PUT     -----------------------

    if request.method == 'PUT':
        id = pk
        ai = Aiquest.objects.get(pk = id)
        # serializer = AiquestSerializer(ai, data = request.data, partial = True) # this will allow   partial update
        serializer = AiquestSerializer(ai, data = request.data) # this need to provide all field even is update one field
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Update Data Successfully"})
        return Response(serializer.errors)

    #-------------------    PATCH     -----------------------

    if request.method == 'PATCH':
        id = pk
        ai = Aiquest.objects.get(pk = id)
        serializer = AiquestSerializer(ai, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Partial Data Update Successfully"})
        return Response(serializer.errors)
    
    #-------------------    DELETE     -----------------------

    if request.method == 'DELETE':
        id = pk
        ai = Aiquest.objects.get(pk = id)
        ai.delete()
        return Response({"msg":"Delete Successfully"})