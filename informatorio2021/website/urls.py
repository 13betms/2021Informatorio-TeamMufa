from django.urls import path
from .views import HomeView,DetalleArticuloView,CrearPostView,ActualizarPostView,EliminarPostView,AñadirComentarioView
#from . import views

urlpatterns = [
    #path('',views.home,name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>',DetalleArticuloView.as_view(),name="detalle articulo"),
    path('añadir_post/', CrearPostView.as_view(),name='añadir post'),
    path('article/edit/<int:pk>',ActualizarPostView.as_view(),name='actualizar post'),
    path('article/<int:pk>/remove',EliminarPostView.as_view(),name='eliminar post'),
    path('article/<int:pk>/comment/', AñadirComentarioView.as_view(),name='añade comentario'),
    
]