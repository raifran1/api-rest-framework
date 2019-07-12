from rest_framework import viewsets
from .serializers import DataAnalizingSerializer
from DataAnalizing.models import DataAnalizing

class DataAnalizingViewSet(viewsets.ModelViewSet):
        queryset = DataAnalizing.objects.all()
        serializer_class = DataAnalizingSerializer