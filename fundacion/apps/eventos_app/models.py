from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)    

modal_choices=[
        (1,"Online"),
        (2,"Presencial"),
    ]

ingr_choices=[
    (1, "Gratuito"),
    (2, "Arancelado"),
]
class Evento(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.PROTECT) 
    titulo = models.CharField(max_length=300) 
    detalle= RichTextField ()
    modalidad = models.PositiveSmallIntegerField (choices= modal_choices, default= 2 )
    lugar=models.CharField(max_length=200)
    ingreso= models.PositiveSmallIntegerField (choices= ingr_choices, default= 1 )
    imag= models.ImageField(null=True, blank=True, upload_to='img/eventos',help_text="Seleccione una imagen para mostrar")  
    categorias= models.ManyToManyField('Categoria', related_name='Evento')

def publicarEvento(self):
        self.publicado = datetime.now()
        self.save()
