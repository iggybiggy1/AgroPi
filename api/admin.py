from django.contrib import admin
from api.models import Plant, DataPoint

# Register your models here.


class DataPointInline(admin.TabularInline):
    model = DataPoint
    extra = 1


class PlantAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Standart Plant information', {
         'fields': ['species', 'name', 'user']}),
        ('Plant Requirements information', {'fields': ['best_temperature', 'temperature_margin', 'best_air_humidity',
                                                       'air_humidity_margin', 'best_soil_moisture', 'soil_moisture_margin', 'best_light', 'light_margin']}),
    ]
    inlines = [DataPointInline]


class DataPointAdmin(admin.ModelAdmin):
    fields = ['air_temperature', 'air_humidity',
              'UV_index', 'soil_moisture', 'plant', 'timestamp']


admin.site.register(Plant, PlantAdmin)
admin.site.register(DataPoint, DataPointAdmin)
