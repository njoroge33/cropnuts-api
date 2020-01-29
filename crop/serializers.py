from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Crate

class CrateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'country',
            'year',
        )
        model = Crate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password')
        extra_kwargs = {'password' : {'write_only': True, 'required': True}}
