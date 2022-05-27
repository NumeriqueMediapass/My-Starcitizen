from django.urls import path

import species
from species.views import list

urlpatterns = [
    path('', species.views.list, name='especes'),
    path('<str:slug>/', species.views.specie_detail, name='espece'),
]
