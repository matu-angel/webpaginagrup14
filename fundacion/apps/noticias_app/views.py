from django.shortcuts import render, redirect
from .models import Noticia, Comentario,Categoria
from apps.eventos_app.models import Evento
from django.contrib.auth.models import User
from django.http.response import Http404
from .forms import FormComentario
from django.contrib.auth.decorators import login_required


def index(request):
    
    lista_noticias = Noticia.objects.all().order_by('-id')[:3]
    lista_eventos = Evento.objects.all().order_by('-id')[:3]
    lista_user = User.objects.all()
    context = {
        "noticias": lista_noticias,
        "eventos": lista_eventos,
        "Usuarios": lista_user
    }
    return render(request, 'index.html', context)


def nosotros(request):
    return render(request, 'nosotros.html')

def noticias(request):
    lista_categorias = Categoria.objects.all()
    lista_noticias = Noticia.objects.all().order_by('-id')
    context = {
        "categorias":lista_categorias,
        "noticias": lista_noticias
    }
    return render(request, 'notices.html', context)


def noticias(request, id):
    try:
        noticia = Noticia.objects.get(id=id)
        lista_comentarios = Comentario.objects.filter(aprobado=True)
    except Noticia.DoesNotExist:
        raise Http404('La Noticia solicitada no existe')\
    
    form = FormComentario()
    
    if (request.method == "POST") and (request.user.id != None):
        form = FormComentario(request.POST)
        if form.is_valid():
            comment = Comentario(
                autor_id = request.user.id,
                cuerpo_comentario=form.cleaned_data["cuerpo_comentario"],
                noticia=noticia
            )
            comment.save()
            return redirect("Noticia", id=noticia.id)

    context = {
        "form":form,
        "noticia": noticia,
        "comentarios": lista_comentarios
    }
    return render(request, 'noticias.html', context)

@login_required
def commentAproved(request, id):
    try:
        comentario = Comentario.objects.get(id=id)
    except Comentario.DoesNotExist:
        raise Http404("Inexistente")

    comentario.aprpove()
    return redirect("Noticia", id=comentario.noticia.id)