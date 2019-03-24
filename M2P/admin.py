from django.contrib import admin

# Register your models here.
from  .models import Sport, Event, Location


admin.site.register(Sport)
admin.site.register(Event)
admin.site.register(Location)