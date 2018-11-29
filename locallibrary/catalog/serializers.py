from catalog.models import Evidence, Evi_case
from rest_framework import serializers

class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidence
        fields = ('evi_case', 'evi_number', 'evi_type', 'summary', 'evi_time', 'signiture', 'picture', 'record')

class EviCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evi_case
        fields = ('number', 'summary')