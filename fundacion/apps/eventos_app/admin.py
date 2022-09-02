from django.contrib import admin
from .models import Categoria, Evento
#from django.utils.safestring import mark_safe

admin.site.register(Categoria)
admin.site.register(Evento)