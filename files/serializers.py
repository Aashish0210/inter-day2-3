from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File  # Use capital 'Meta' to define the model
        fields = ['id', 'name', 'path', 'size', 'type', 'date']  # List the fields you want to serialize
