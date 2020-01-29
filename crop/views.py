from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status
from .serializers import SampleSerializer
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from .models import Sample

class SampleList(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

    def post(self,request):
        serializer = SampleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

