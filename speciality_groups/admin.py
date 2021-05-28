from django.contrib import admin
from .models import Adviser, Group, Enrollment, Grades, Group_Enrollment, StudentGpa
# Register your models here.

class AdviserAdmin(admin.ModelAdmin):
    pass
admin.site.register(Adviser, AdviserAdmin)

class GroupAdmin(admin.ModelAdmin):
    pass
admin.site.register(Group, GroupAdmin)

class EnrollmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Enrollment, EnrollmentAdmin)

class GradesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Grades, GradesAdmin)

class EnrollmentGroupAdmin(admin.ModelAdmin):
    pass
admin.site.register(Group_Enrollment, EnrollmentGroupAdmin)

class StudentGpaAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentGpa, StudentGpaAdmin)