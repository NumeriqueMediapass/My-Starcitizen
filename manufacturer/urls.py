from django.urls import path

import manufacturer
from manufacturer.views import list

urlpatterns = [
    path('', manufacturer.views.list, name='fabriquants'),
    path('<str:slug>/', manufacturer.views.manufacturer_detail, name='fabriquant'),
]
