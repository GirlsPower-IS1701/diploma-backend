from django.contrib import admin
from .models import Department, Subject_Cycles, Subjects, Cafedra_Subjects

class DepartmentAdmin(admin.ModelAdmin):
    pass
    list_display = ('name', 'short_name')
admin.site.register(Department, DepartmentAdmin)

class SubjectCyclesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Subject_Cycles, SubjectCyclesAdmin)

class SubjectsAdmin(admin.ModelAdmin):
    pass
    list_display = ('title', 'code', 'department_id', 'lection_count', 'lab_count', 'practice_count', 'credits_count')
    search_fields = ['title', 'code']
admin.site.register(Subjects, SubjectsAdmin)

class CafedraSubjectsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cafedra_Subjects, CafedraSubjectsAdmin)