from catalog.models import Evidence
from rest_framework import serializers

class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidence
        fields = ('evi_case', 'evi_number', 'evi_type', 'summary', 'evi_time', 'signiture', 'picture', 'record')