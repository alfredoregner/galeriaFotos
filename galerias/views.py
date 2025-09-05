from django.shortcuts import render, get_object_or_404
from .models import Galeria


def home(request):
    galerias=Galeria.objects.all()
    return render(request, 'galerias/home.html', {'galerias':galerias})

def galeria_detail(request, id):
    galeria = get_object_or_404(Galeria, pk = id)
    context={
        'galeria': galeria,
    }
    return render(request, 'galerias/galeria_detail.html', context)

def pesquisar_galerias(request):
    query = request.GET.get('q') # pega o que foi digitado no campo de busca
    resultados = []

    if query:
        # filtrar receitas que contenham o termo no nome (sem case-sensitive)
        resultados = Galeria.objects.filter(car__icontains=query)

    context = {
        'query': query,
        'resultados': resultados,
    }
    return render(request, 'galerias/pesquisa.html', context)