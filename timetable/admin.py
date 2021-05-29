from django.contrib import admin
from .models import Timetable


class TimetableAdmin(admin.ModelAdmin):
    pass

    list_display = ('day_of_week', 'lesson_type', 'start_time', 'finish_time', 'room_number')
admin.site.register(Timetable, TimetableAdmin)
