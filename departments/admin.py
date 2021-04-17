from django.contrib import admin
from .models import Department, Subject_Cycles, Subjects, Cafedra_Subjects

class DepartmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Department, DepartmentAdmin)

class SubjectCyclesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Subject_Cycles, SubjectCyclesAdmin)

class SubjectsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Subjects, SubjectsAdmin)

class CafedraSubjectsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cafedra_Subjects, CafedraSubjectsAdmin)