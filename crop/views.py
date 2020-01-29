from django.shortcuts import render
from rest_framework import generics
from .models import Crate
from .serializers import CrateSerializer


class ListCrate(generics.ListCreateAPIView):
    queryset = Crate.objects.all()
    serializer_class = CrateSerializer


class DetailCrate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crate.objects.all()
    serializer_class = CrateSerializer