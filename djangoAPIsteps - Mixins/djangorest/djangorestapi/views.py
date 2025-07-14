from django.shortcuts import render
from . models import Aiquest
from . serializers import AiquestSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

# Create your views here.

# for get  all data
class AiquestList(GenericAPIView,ListModelMixin):
    queryset = Aiquest.objects.all()
    serializer_class =  AiquestSerializer

    def get(self, request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
# for get model instance(selected id) data
class AiquestRetrive(GenericAPIView,RetrieveModelMixin):
    queryset = Aiquest.objects.all()
    serializer_class =  AiquestSerializer

    def get(self, request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

# for post
class AiquestCreate(GenericAPIView,CreateModelMixin):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer
    
    def post(self, request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
# for put
class AiquestUpdate(GenericAPIView,UpdateModelMixin):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer
    
    def put(self, request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    

# for delete
class AiquestDestroy(GenericAPIView,DestroyModelMixin):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer
    
    def delete(self, request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
    

# for CRUD

class AiquestList_Creat(GenericAPIView,ListModelMixin, CreateModelMixin):

    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer

    def get(self, request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self, request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
class AiquestRetrieve_Update_Destroy(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):

    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer
    
    def get(self, request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self, request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self, request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
    