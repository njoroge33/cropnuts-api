from rest_framework import serializers
from .models import Sample

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ('id', 'user', 'batch_number', 'sample_type', 'client', 'location', 'description', 'receipt_date', 'archival_date')