
from rest_framework import serializers


class enquiry_tableSerializer(serializers.Serializer):
    # Rememer serializers.Serializer - S is capital of Serializer
    name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=10)

