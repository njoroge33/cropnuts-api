from rest_framework import serializers
from .models import Crate


class CrateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'country',
            'year',
        )
        model = Crate