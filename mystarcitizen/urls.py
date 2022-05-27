from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import accounts.views
from blog.views import index, import_data
from mystarcitizen import settings


urlpatterns = [
    path('', index, name='index'),
    path('import/', import_data, name='import'),
    path('deconnexion/', accounts.views.logout_user, name='logout'),
    path('inscription/', accounts.views.register, name='register'),
    path('connexion/', accounts.views.login_view, name='login'),
    path('fabriquants/', include('manufacturer.urls')),
    path('especes/', include('species.urls')),
    path('vaisseaux/', include('ship.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
