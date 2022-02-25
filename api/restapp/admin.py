from django.contrib import admin
from api.restapp.models import Distance

# Register your models here.
@admin.register(Distance)
class DistanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'city1', 'city2', 'dist']