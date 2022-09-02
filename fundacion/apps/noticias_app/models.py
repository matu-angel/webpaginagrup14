from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)    # tabla categoria que contiene NOMBRE 

def __string__ (self):
        print(self.nombre)
        return self.nombre

class Noticia(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE) #CLAVE SEGUNDARIA , USUARIO (CREA LA NOTICIA) Y CUANDO SE ELIMINA CATEGORIA SE ELIMINA EL AUTOR
    titulo = models.CharField(max_length=255) 
    contenido = RichTextField () 
    imag = models.ImageField(null=True, blank=True, upload_to='img/noticias',help_text="Seleccione una imagen para mostrar")  #mostrar imagen , null=true si quiere poner , lugar de la imagen 
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)
    publicado = models.DateTimeField(blank=True, null=True)
    categorias = models.ManyToManyField('Categoria', related_name='noticias') 

    def publicarNoticia(self):
        self.publicado = datetime.now()
        self.save()

    def comentariosAprobados(self):             
        return self.comentarios.filter(aprobado=True)

class Comentario(models.Model):
    noticia = models.ForeignKey('Noticia',related_name='comentario', on_delete=models.CASCADE)
    autor =  models.ForeignKey('auth.User', on_delete=models.CASCADE)
    cuerpo_comentario = models.TextField()
    creado = models.DateTimeField(default=timezone.now)
    aprobado = models.BooleanField(default=False) #MODERADO 

    def aprobarComentarios(self): #MODERACION
        self.aprobado = True
        self.save()