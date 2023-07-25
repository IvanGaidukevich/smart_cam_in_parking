from django.contrib import admin

from scip.models import Vehicle, Owner, Arrive, Departure


class ArriveInline(admin.StackedInline):
    model = Arrive


class DepartureInline(admin.StackedInline):
    model = Departure


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('number', 'model_name', 'color', 'info')
    list_filter = ('color',)
    fields = [('type', 'model_name', 'color'), 'number', 'info']
    inlines = [ArriveInline, DepartureInline]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'tel')


@admin.register(Arrive)
class ArriveAdmin(admin.ModelAdmin):
    list_display = ('time', 'vehicle')
    list_filter = ('time', 'vehicle')


@admin.register(Departure)
class DepartureAdmin(admin.ModelAdmin):
    list_display = ('time', 'vehicle')
    list_filter = ('time', 'vehicle')


# Register your models here.
# admin.site.register(Vehicle)
# admin.site.register(Owner)
# admin.site.register(Entry)
# admin.site.register(Exit)
