from django.contrib import admin
#from django.utils.safestring import mark_safe
from .models import Categoria, Comentario, Noticia
from apps.noticias_app import models

class CategoriasAdmin (admin.ModelAdmin):
    list_display=("nombre",) #muestre

admin.site. register(Categoria, CategoriasAdmin)

class NoticiasAdmin(admin.ModelAdmin):
    list_display =("titulo","autor","imag")
    search_fields=("titulo", "autor","creado") #buscar

lis_per_page= 20 #pagina

readonly_fields=["noticias_imag"] #miniatura de la imagen
"""""
def noticias_img(self,obj):
    return mark_safe(
        "<a href="{0}"><imag src="{0}" width="30%"></a>".format(self.img.url)
    ) #mostrar la imagen anteriormente mencionada
"""

admin.site.register (Noticia,NoticiasAdmin)

class ComentarioAdmin(admin.ModelAdmin):
        list_display=("autor","cuerpo_comentario", "noticia", "creado", "aprobado")
        list_filter= ("aprobado", "creado")    #ver los filtros
        search_fields=("cuerpo_comentario", "autor") #para buscar palabras claves
        actions=['aprobar_comentarios']
        def aprobar_comentarios(self, request, queryset):        #para ver los aprobados
            queryset.update (aprobado=True)

admin.site.register(Comentario,ComentarioAdmin)