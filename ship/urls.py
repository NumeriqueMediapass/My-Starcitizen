from django.urls import path

import ship
from ship.views import list

urlpatterns = [
    path('', ship.views.list, name='vaisseaux'),
    path('<str:slug>/', ship.views.ship_detail, name='vaisseau'),
]
