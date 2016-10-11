from django.shortcuts import render
from django.utils import timezone
from .models import Post #Se puede utilizar .models debido a que views.py y models.py
                         #se encuentran en el mismo directorio.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #Lista de entradas del blog que han sido publicadas y ordenadas por fecha de publicación.
    return render(request, 'blog/post_list.html', {'posts':posts})
