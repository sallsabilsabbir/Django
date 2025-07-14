from django.shortcuts import render
from . models import Aiquest
from . serializers import AiquestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class AiquestCreate(APIView):

    #-------------------    GET     -----------------------

    def get(self, request, pk= None, format= None ):
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
    
    def post(self, request, format= None ):
        serializer = AiquestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Successfully Insert Data"})
        return Response(serializer.errors)
    

    #-------------------     PUT     -----------------------

    def put(self, request, pk, format= None ):
        id = pk
        ai = Aiquest.objects.get(pk = id)
        # serializer = AiquestSerializer(ai, data = request.data, partial = True) # this will allow   partial update
        serializer = AiquestSerializer(ai, data = request.data) # this need to provide all field even is update one field
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Update Data Successfully"})
        return Response(serializer.errors)

    #-------------------    PATCH     -----------------------

    def patch(self, request, pk, format= None ):
        id = pk
        ai = Aiquest.objects.get(pk = id)
        serializer = AiquestSerializer(ai, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Partial Data Update Successfully"})
        return Response(serializer.errors)
    
    #-------------------    DELETE     -----------------------

    def delete(self, request, pk, format= None ):
        id = pk
        ai = Aiquest.objects.get(pk = id)
        ai.delete()
        return Response({"msg":"Delete Successfully"})