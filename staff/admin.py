from django.contrib import admin
from .models import Academic_Degree, Academic_Rank, Position_Types, Positions, Staff
# Register your models here.

class AcademicDegreeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Academic_Degree, AcademicDegreeAdmin)

class AcademicRankAdmin(admin.ModelAdmin):
    pass
admin.site.register(Academic_Rank, AcademicRankAdmin)

class PositionTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Position_Types, PositionTypeAdmin)

class PositionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Positions, PositionAdmin)

class StaffAdmin(admin.ModelAdmin):
    pass
admin.site.register(Staff, StaffAdmin)
