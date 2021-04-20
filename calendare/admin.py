from django.contrib import admin
from .models import Academic_Calendar, Events
# Register your models here.

class AcademicCalendarAdmin(admin.ModelAdmin):
    pass
admin.site.register(Academic_Calendar, AcademicCalendarAdmin)

class EventsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Events, EventsAdmin)