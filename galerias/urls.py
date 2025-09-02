from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('galeria/<int:id>/', views.galeria_detail, name='galeria_detail'),
    path('pesquisa/', views.pesquisar_galerias, name='pesquisar_galerias'),
]

# Adicionar galerias de imagens 