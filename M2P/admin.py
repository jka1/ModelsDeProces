from django.contrib import admin

# Register your models here.
from .models import Sport, Event, Location, DateTime

admin.site.register(Sport)
admin.site.register(Event)
admin.site.register(Location)
admin.site.register(DateTime)