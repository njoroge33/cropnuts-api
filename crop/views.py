from django.shortcuts import render
from .serializers import CrateSerializer, UserSerializer, SampleSerializer
from django.contrib.auth.models import User
from .models import Crate, Sample
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets

class SampleList(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ["batch_number"]

    def post(self, request):
        serializer = SampleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListCrate(viewsets.ModelViewSet):
    queryset = Crate.objects.all()
    serializer_class = CrateSerializer
    
    def post(self,request):
        serializer = CrateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
          
@api_view(['GET', 'POST'])
def login(request):
    permission_classes = (IsAuthenticated,)
    users = User.objects.all()

    if request.method == "POST":
        data = request.data
        username = data.get('username')
        pass_secure = data.get('password')
        users = User(username=username, password=pass_secure)
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return Response('bad credentials', status=status.HTTP_401_UNAUTHORIZED)
        if user:
            if user.password == pass_secure:
                users=User(username=username, password=pass_secure, id=user.id)
                token = RefreshToken.for_user(users)
                return JsonResponse({'message':'loggedin!!', 'token': str(token.access_token), 'status':status.HTTP_200_OK})
    return Response('bad credentials', status=status.HTTP_401_UNAUTHORIZED)