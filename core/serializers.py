"""
Serializers for Emissions API
"""

from rest_framework import serializers
from core.models import Emission

class EmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Emission
        fields = ['id', 'date_created', 'accounting_period', 'scope_1', 'scope_2', 'scope_3']
        