from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Comment, Post
from .forms import PostForm,CommentForm
from django.urls import reverse_lazy

#def home(request):
#   return render(request,'home.html',{})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering=['-fecha_publicacion']

class DetalleArticuloView(DetailView):
    model = Post
    template_name = 'detalle_articulo.html'

class CrearPostView(CreateView):
    model = Post
    #form_class = PostForm
    template_name = 'añadir_post.html'
    fields = '__all__'

class ActualizarPostView(UpdateView):
    model = Post
    #form_class = PostForm
    template_name='actualizar_post.html'
    fields=['titulo','cuerpo']

class EliminarPostView(DeleteView):
    model=Post
    template_name='eliminar_post.html'
    success_url = reverse_lazy('home')

class AñadirComentarioView(CreateView):
    model = Comment
    form_class=CommentForm
    template_name = 'añade_comentario.html'
    #fields = '__all__'
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)




