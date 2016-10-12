from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post #Se puede utilizar .models debido a que views.py y models.py
                         #se encuentran en el mismo directorio.
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #Lista de entradas del blog que han sido publicadas y ordenadas por fecha de publicación.
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST": #View con los datos del formulario que acabamos de escribir.
        form = PostForm(request.POST) #Construimos el PostForm con los datos del formulario.
        if form.is_valid(): #Comprobación de que todos los datos campos necesarios están definidos
                            #y no hay valores incorrectos.
            post = form.save(commit=False) #No guardamos el modelo Post todavía, ya que queremos
                                           #añadir en primer lugar el autor.
            post.author = request.user #Añadimos el autor.
            post.published_date = timezone.now()
            post.save() #Guardamos los cambios añadiendo el autor y se creará un nuevo post en el blog.
            return redirect('blog.views.post_detail', pk=post.pk)
    else: #Acceso a la página por primera vez para la creación de un formulario en blanco.
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
