from django.shortcuts import render
from core import serializers
from core.models import Emission
from rest_framework import viewsets
# Create your views here.


class EmissionViewSet(viewsets.ModelViewSet):
    """View for emission apis"""

    serializer_class = serializers.EmissionSerializer
    queryset = Emission.objects.all()

    def get_queryset(self):
        """Retrieve emissions"""
        return self.queryset.filter().order_by('-id')
