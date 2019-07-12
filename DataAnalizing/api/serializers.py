from rest_framework import serializers
from DataAnalizing.models import DataAnalizing

class DataAnalizingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAnalizing
        fields = '__all__'