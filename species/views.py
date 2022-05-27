from django.shortcuts import render, get_object_or_404
from species.models import Species


def list(request):
    species = Species.objects.all()
    return render(request, 'species/list.html', context={'species': species})


def specie_detail(request, slug):
    specie = get_object_or_404(Species, slug=slug)
    return render(request, 'species/detail.html', context={'specie': specie})
