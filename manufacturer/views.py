from django.shortcuts import render, get_object_or_404
from manufacturer.models import Manufacturer
from ship.models import Ship
from species.models import Species


def list(request):
    manufacturers = Manufacturer.objects.all()
    return render(request, 'manufacturer/list.html', context={'manufacturers': manufacturers})


def manufacturer_detail(request, slug):
    manufacturer = get_object_or_404(Manufacturer, slug=slug)
    ships = Ship.objects.filter(manufacturer=manufacturer)
    return render(request, 'manufacturer/detail.html', context={
        'manufacturer': manufacturer,
        'ships': ships,
    })
