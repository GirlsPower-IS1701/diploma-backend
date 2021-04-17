from django.contrib import admin
from .models import Room_Type, Room, Lession_Time, TimeTable
# Register your models here.

class RoomTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Room_Type, RoomTypeAdmin)

class RoomAdmin(admin.ModelAdmin):
    pass
admin.site.register(Room, RoomAdmin)

class LessionTimeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Lession_Time, LessionTimeAdmin)

class TimetableAdmin(admin.ModelAdmin):
    pass
admin.site.register(TimeTable, TimetableAdmin)
