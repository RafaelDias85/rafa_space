from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia 


def index(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True) 
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar'] #Referencia ao name='buscar'
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar) #O argumento nome__icontains irá buscar se, dentro do nome
                                                                            #que estamos conferindo de um objeto em específico, existe 
                                                                            #alguma parte que faz sentido com o nome que está sendo buscado. 
                                                                            # Ele irá buscar se pelo menos metade do nome faz sentido em relação ao que estamos buscando.
    return render(request, "galeria/buscar.html", {"cards": fotografias})