from django.shortcuts import render
from django.contrib.auth.models import User
# from rest_framework import generics, status
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
​
class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
​
​
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
