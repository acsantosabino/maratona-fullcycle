from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from django.views import generic

from .models import Aulas

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'maratona/index.html'
    context_object_name = 'lista_aulas'

    def get_queryset(self):
        return Aulas.objects.all()