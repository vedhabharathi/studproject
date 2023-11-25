from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import Student
from .serializers import StudentSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List':'/Studentlist/',
        'Detail View':'/Studentdetail/<str:pk>/',
        'Create':'/Studentcreate/',
        'Update':'/Studentupdate/<str:pk>/',
        'Delete':'/Studentdelete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def itemList(request):
    item=Student.objects.all()
    serializer=StudentSerializer(item,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def itemDetail(request,pk):
    item=Student.objects.get(id=pk)
    serializer=StudentSerializer(item,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def itemCreate(request):
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def itemUpdate(request,pk):
    item=Student.objects.get(id=pk)
    serializer=StudentSerializer(instance=item,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def itemDelete(request,pk):
    item=Student.objects.get(id=pk)
    item.delete()
    return Response('Item Deleted')