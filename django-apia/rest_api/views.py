from msilib.schema import ServiceInstall
from urllib import response
from django.shortcuts import render

# rest
from .serializers import KrosovkaAPI
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from .models import Krosovka
from rest_framework import generics
from rest_framework import filters

def home(request):
    return render(request, 'home.html')

# API to'liq chiqarish

@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def krosovkaMakeApi(request):
    krosovka = Krosovka.objects.all()
    serializer = KrosovkaAPI(krosovka, many=True)
    return Response(serializer.data)

# API ni alohida chiqarish

@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def singleAPI(request, pk):
    krosovka = Krosovka.objects.get(id=pk)
    serializers = KrosovkaAPI(krosovka, many=False)
    return Response(serializers.data)

# post joylash, (ma'lumot joylash)
@api_view(["POST"])
@permission_classes((permissions.AllowAny, ))
def malumotJoylash(request, pk):
    krosovka = Krosovka.objects.get(id=pk)
    serializer = KrosovkaAPI(instance=krosovka, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return response(serializer.data)

# post update qilish
@api_view(["POST"])
@permission_classes((permissions.AllowAny, ))
def malumotupdate(request, pk):
    krosovka = Krosovka.objects.get(id=pk)
    serializer = KrosovkaAPI(instance=krosovka, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return response(serializer.data)

# post delete qilish
@api_view(["DELETE"])
@permission_classes((permissions.AllowAny, ))
def malumotDelete(request, pk):
    krosovka = Krosovka.objects.get(id=pk)
    krosovka.delete()
        
    return Response("Muvoffaqiyatli o'chirildi.")

# rest api filter
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def filterKrosovka(request):
    filter = Krosovka.objects.filter(turi='BAZM')
    serializer = KrosovkaAPI(filter, many=True)
    return Response(serializer.data)
    
    
# search api

class KrocsovkaSearchAPI(generics.ListAPIView):
    queryset = Krosovka.objects.all()
    serializer = KrosovkaAPI
    filter_backends = [filters.SearchFilter]
    search_fileds = ['brand', 'color']
    
krosovkaSearch = KrocsovkaSearchAPI.as_view()