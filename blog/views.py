import random
from django.shortcuts import render, redirect

import ship
from blog.models import Blog
from ship.models import Role, Ship, Status
from species.models import Species
from manufacturer.models import Manufacturer
from faker import Faker


# Page d'accueil du site
def index(request):
    posts = Blog.objects.all()

    return render(request, 'blog/index.html', context={'posts': posts})


# Page pour importer des données
def import_data(request):
    # global new_species, new_role, new_manufacturer, new_ship, new_status
    faker = Faker()

    for _ in range(10):
        name = 'Espèce ' + str(_)
        slug = faker.slug() + '-' + str(_)
        description = faker.text()
        Species.objects.create(name=name, description=description, slug=slug)

    for _ in range(10):
        name = 'Role ' + str(_)
        description = faker.text()
        Role.objects.create(name=name, description=description)

    for _ in range(4):
        name = 'Statut ' + str(_)
        Status.objects.create(name=name)

    for _ in range(7):
        # Récupération des espèces aléatoires
        items = list(Species.objects.all())
        new_species = random.sample(items, 3)
        new_species = random.choice(items)

        name = 'Manufacturer ' + str(_) + ' ' + faker.company()
        slug = faker.slug() + '-' + str(_)
        logo = faker.image_url()
        date_created = faker.date_time()
        code = faker.ean8()
        founder = faker.name()
        headquarters = faker.address()
        activities = faker.text()
        summary = faker.text()
        history = faker.text()
        spacie = new_species
        Manufacturer.objects.create(
            name=name,
            slug=slug,
            logo=logo,
            date_created=date_created,
            code=code,
            founder=founder,
            headquarters=headquarters,
            activities=activities,
            summary=summary,
            history=history,
            spacie=spacie
        )

    for _ in range(10):
        items = list(Status.objects.all())
        new_status = random.sample(items, 3)
        new_status = random.choice(items)

        items = list(Role.objects.all())
        new_role = random.sample(items, 3)
        new_role = random.choice(items)

        items = list(Manufacturer.objects.all())
        new_manufacturer = random.sample(items, 3)
        new_manufacturer = random.choice(items)

        name = 'Vaisseau ' + str(_)
        slug = faker.slug() + '-' + str(_)
        length = '3'
        width = '3'
        height = '3'
        empty_mass = '3'
        cargo_capacity = '3'
        crew_capacity = '3'
        crew_capacity_max = '9'
        logo = faker.image_url()
        manufacturer = new_manufacturer
        role = new_role
        status = new_status
        Ship.objects.create(
            name=name,
            slug=slug,
            length=length,
            width=width,
            height=height,
            empty_mass=empty_mass,
            cargo_capacity=cargo_capacity,
            crew_capacity=crew_capacity,
            crew_capacity_max=crew_capacity_max,
            logo=logo,
            manufacturer=manufacturer,
            status=status,
            role=role
        )

    return redirect('index')
