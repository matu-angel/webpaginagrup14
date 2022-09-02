from django.shortcuts import render
#from .models import Evento
#from django.http.response import Http404

def eventos(request):
    return render(request, 'eventos.html', {})
