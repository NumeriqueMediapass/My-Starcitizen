from django.contrib import admin

# Register your models here.
from species.models import Species


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('name', 'governance')
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Species, SpeciesAdmin)
