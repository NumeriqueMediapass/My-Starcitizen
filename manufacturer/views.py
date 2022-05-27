from django.shortcuts import render, get_object_or_404
from manufacturer.models import Manufacturer


def list(request):
    manufacturers = Manufacturer.objects.all()
    return render(request, 'manufacturer/list.html', context={'manufacturers': manufacturers})


def manufacturer_detail(request, slug):
    manufacturer = get_object_or_404(Manufacturer, slug=slug)
    return render(request, 'manufacturer/detail.html', context={'manufacturer': manufacturer})
