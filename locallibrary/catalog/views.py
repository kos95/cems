from django.shortcuts import render

# Create your views here.

from catalog.models import Evidence, Evi_type, Evi_case

def index(request):
    """view func for homepage of site."""

    num_evi = Evidence.objects.all().count()
    num_type = Evidence.objects.all().count()
    num_case = Evidence.objects.all().count()

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


