from rest_framework import viewsets
from .serializers import EmailSerializer
from Email.models import Email

class EmailViewSet(viewsets.ModelViewSet):
        queryset = Email.objects.all()
        serializer_class = EmailSerializer