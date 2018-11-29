from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from catalog.models import Evidence, Evi_type, Evi_case
from catalog.serializers import EvidenceSerializer, EviCaseSerializer

def index(request):
    """view func for homepage of site."""

    num_evi = Evidence.objects.all().count()
    num_type = Evi_type.objects.all().count()
    num_case = Evi_case.objects.all().count()

    context = {
        'num_evi':num_evi,
        'num_type':num_type,
        'num_case':num_case,
    }
    
    return render(request, 'index.html', context=context)

from django.views import generic

class CaseEviView(generic.ListView):
    model = Evi_case

class CaseDetailView(generic.DetailView):
    model = Evi_case

class EvidenceViewSet(viewsets.ModelViewSet):
    queryset = Evidence.objects.all()
    serializer_class = EvidenceSerializer

class EviCaseViewSet(viewsets.ModelViewSet):
    queryset = Evi_case.objects.all()
    serializer_class = EviCaseSerializer

class EvidenceView(generic.ListView):
    model = Evidence

class EvidenceDetailView(generic.DetailView):
    model = Evidence
