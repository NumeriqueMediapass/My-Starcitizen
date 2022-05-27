from django.contrib import admin
from ship.models import Ship, Status


class ShipAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'manufacturer')
    list_filter = ('status',)
    search_fields = ('name',)
    verbose_name = 'Vaisseaux'


admin.site.register(Status)
admin.site.register(Ship, ShipAdmin)
