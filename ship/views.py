from django.shortcuts import render, get_object_or_404
from ship.models import Ship


def list(request):
    ships = Ship.objects.all()
    return render(request, 'ship/list.html', context={'ships': ships})


def ship_detail(request, slug):
    ship = get_object_or_404(Ship, slug=slug)
    return render(request, 'ship/detail.html', context={'ship': ship})
